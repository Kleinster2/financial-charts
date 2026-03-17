import os, re, json

vault = 'investing'
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(out_dir, exist_ok=True)

# 1. Collect all stubs
stubs = []
for root, dirs, files in os.walk(vault):
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f).replace(os.sep, '/')
        try:
            lines = len(open(path, encoding='utf-8').readlines())
            if lines <= 25:
                stubs.append({'path': path, 'name': f[:-3], 'lines': lines})
        except:
            pass

# 2. Count backlinks for each stub
all_content = ''
for root, dirs, files in os.walk(vault):
    for f in files:
        if not f.endswith('.md'):
            continue
        try:
            all_content += open(os.path.join(root, f), encoding='utf-8').read()
        except:
            pass

for s in stubs:
    name = s['name']
    pattern = re.escape(name)
    refs = len(re.findall(r'\[\[' + pattern + r'(\|[^\]]+)?\]\]', all_content))
    s['refs'] = refs

# 3. Sort by refs descending
stubs.sort(key=lambda x: -x['refs'])

# 4. Save full list
with open(os.path.join(out_dir, 'remaining_stubs.json'), 'w', encoding='utf-8') as fp:
    json.dump(stubs, fp, indent=2, ensure_ascii=False)

# 5. Create batches of 25
num_batches = (len(stubs) + 24) // 25
for i in range(0, len(stubs), 25):
    batch = stubs[i:i+25]
    batch_num = i // 25
    with open(os.path.join(out_dir, f'batch_{batch_num}.json'), 'w', encoding='utf-8') as fp:
        json.dump(batch, fp, indent=2, ensure_ascii=False)

print(f'Output dir: {out_dir}')
print(f'Total stubs: {len(stubs)}')
print(f'Batches: {num_batches}')
for s in stubs[:10]:
    print(f'  {s["refs"]:3d} refs | {s["name"]}')
