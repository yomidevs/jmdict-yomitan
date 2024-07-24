import { $ } from 'bun';

import * as path from 'path';
import { readdir } from 'fs/promises';

const URL_PREFIX =
  'https://github.com/themoeway/jmdict-yomitan/releases/latest/download/';
const JSON_FILE = (dictName: string) => `${dictName}.json`;
const JSON_URL = (dictName: string) => `${URL_PREFIX}${dictName}.json`;
const ZIP_URL = (dictName: string) => `${URL_PREFIX}${dictName}.zip`;
const DEST_DIR = 'dst';
const TMP_DIR = 'tmp';
const INDEX_JSON = 'index.json';

const files = await readdir(DEST_DIR);
for (const file of files) {
  const zipPath = path.join(DEST_DIR, file);
  const dictName = file.replace('.zip', '');

  await $`rm -rf ${TMP_DIR}`;
  await $`mkdir -p ${TMP_DIR}`;
  await $`unzip -d ${TMP_DIR} ${zipPath}`;

  const indexJsonPath = path.join(TMP_DIR, INDEX_JSON);
  const indexJson = await Bun.file(indexJsonPath).json();

  // Modify index.json with auto update info
  indexJson.isUpdatable = true;
  indexJson.indexUrl = JSON_URL(dictName);
  indexJson.downloadUrl = ZIP_URL(dictName);
  await Bun.write(indexJsonPath, JSON.stringify(indexJson));
  // Copy index.json to /dst and rename to JSON_FILE
  await $`cp ${indexJsonPath} ${DEST_DIR}/${JSON_FILE(dictName)}`;

  // Zip archive back to zipPath at max compression
  await $`cd ${TMP_DIR} && zip -r -9 ${file} .`;
  await $`mv ${TMP_DIR}/${file} ${DEST_DIR}`;

  await $`rm -rf ${TMP_DIR}`;
}
