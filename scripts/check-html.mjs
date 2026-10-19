import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';

const html = readFileSync(new URL('../blockforge_studio.html', import.meta.url), 'utf8');
assert.match(html, /<title>BlockForge Studio/);
for (const [id, label] of [
  ['paletteSearch', 'searchable block palette'],
  ['examplesBtn', 'starter examples'],
  ['runBtn', 'Python run control'],
  ['runOutput', 'program output panel'],
  ['zoomInBtn', 'workspace zoom controls'],
  ['codePreview', 'generated code preview'],
]) {
  assert.match(html, new RegExp('id="' + id + '"'), label + ' exists');
}
assert.match(html, /blockforge-v2-draft/, 'browser-local autosave key exists');
assert.match(html, /version:2/, 'new projects use version 2');
assert.match(html, /5\*1024\*1024/, 'project import size limit exists');
assert.match(html, /seen\.has\(b\.id\)/, 'duplicate block IDs are rejected');
assert.match(html, /fetch\('\/api\/run'/, 'run button calls the local runner API');
assert.doesNotMatch(html, /https?:\/\/(?:unpkg\.com|cdnjs\.cloudflare\.com|cdn\.jsdelivr\.net)/, 'editor must not require common external CDNs');

const defsStart = html.indexOf('const DEFS = {');
const defsEnd = html.indexOf('const CATEGORY_BLOCKS', defsStart);
const defsSource = html.slice(defsStart, defsEnd);
const blockTypes = [...defsSource.matchAll(/^\s*([A-Za-z_]\w*):\{cat:/gm)].map((match) => match[1]);
const generatorStart = html.indexOf('function generate()');
const generatorEnd = html.indexOf('function updateCode()', generatorStart);
const generatorSource = html.slice(generatorStart, generatorEnd);
const generatedTypes = new Set([...generatorSource.matchAll(/case'([^']+)'/g)].map((match) => match[1]));
assert.ok(blockTypes.length > 0, 'block definitions are discoverable');
for (const type of blockTypes) {
  assert.ok(generatedTypes.has(type), 'block type has an explicit code-generation case: ' + type);
}

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
assert.equal(scripts.length, 1, 'the single-file editor should contain one inline script');
new Function(scripts[0][1]); // Parse only; do not execute the browser application in CI.

console.log('BlockForge static checks passed.');
