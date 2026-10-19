import { readFileSync } from 'node:fs';
import assert from 'node:assert/strict';

const html = readFileSync(new URL('../blockforge_studio.html', import.meta.url), 'utf8');
assert.match(html, /<title>BlockForge Studio/);
assert.match(html, /id="paletteSearch"/, 'block palette search input exists');
assert.match(html, /id="examplesBtn"/, 'examples button exists');
assert.match(html, /blockforge-v2-draft/, 'browser-local autosave key exists');
assert.match(html, /version:2/, 'new projects use version 2');
assert.match(html, /5\*1024\*1024/, 'project import size limit exists');
assert.match(html, /seen\.has\(b\.id\)/, 'duplicate block IDs are rejected');

const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/gi)];
assert.equal(scripts.length, 1, 'the single-file editor should contain one inline script');
new Function(scripts[0][1]); // Parse only; do not execute the application in CI.

console.log('BlockForge static checks passed.');
