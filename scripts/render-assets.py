"""Regenerate the profile's self-contained SVG illustrations with Python 3."""
from pathlib import Path

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
THEMES = {
    'dark': dict(bg='#111c2b', panel='#18293a', text='#f1f5f6', muted='#b3c4ce', accent='#85e0c4', warm='#f1ba91', line='#344b5b', grid='#293d4d', wash='#203c42'),
    'light': dict(bg='#f6f4ee', panel='#ffffff', text='#182e3b', muted='#516773', accent='#176c5a', warm='#9a5129', line='#c8d5d1', grid='#dce3dc', wash='#e4eee5'),
}

def wrap(title, desc, height, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
<title id="title">{title}</title><desc id="desc">{desc}</desc>
<style>text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif; }} .mono {{ font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', monospace; }}</style>
{body}
</svg>
'''

def header(c):
    body = f'''<defs>
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{c['grid']}" /></pattern>
<linearGradient id="wash" x1="0" y1="0" x2="1" y2="1"><stop stop-color="{c['wash']}" /><stop offset="1" stop-color="{c['bg']}" /></linearGradient>
</defs>
<rect width="1200" height="380" rx="24" fill="{c['bg']}" />
<path d="M730 0H1176Q1200 0 1200 24V356Q1200 380 1176 380H730Z" fill="url(#wash)" />
<rect x="720" y="20" width="460" height="340" fill="url(#grid)" />
<rect x="56" y="48" width="28" height="4" rx="2" fill="{c['accent']}" />
<text x="98" y="55" fill="{c['accent']}" class="mono" font-size="14" letter-spacing="2">AI FULL-STACK ENGINEER</text>
<text x="52" y="162" fill="{c['text']}" font-size="88" font-weight="700" letter-spacing="-4">Jack Ou<tspan fill="{c['accent']}">.</tspan></text>
<text x="56" y="214" fill="{c['muted']}" font-size="25">From database internals</text>
<text x="56" y="248" fill="{c['muted']}" font-size="25">to AI products.</text>
<path d="M56 284H630" stroke="{c['line']}" />
<text x="56" y="326" fill="{c['accent']}" class="mono" font-size="14" letter-spacing="1">CONTEXT / AGENTS / SYSTEMS</text>
<text x="56" y="351" fill="{c['muted']}" class="mono" font-size="12">SHENZHEN, CN · JACK-OUCJ</text>
<path d="M820 102H787V288H820M787 195H840" fill="none" stroke="{c['accent']}" stroke-width="2" />
<circle cx="787" cy="195" r="5" fill="{c['accent']}" />'''
    for x, y, width, label, name, color in [
        (820, 60, 312, '01 / THE EXPERIENCE', 'AI products', c['accent']),
        (840, 153, 292, '02 / THE INTELLIGENCE', 'Agent workflows', c['warm']),
        (820, 246, 312, '03 / THE FOUNDATION', 'Systems engineering', c['accent']),
    ]:
        body += f'''\n<rect x="{x}" y="{y}" width="{width}" height="84" rx="12" fill="{c['panel']}" stroke="{c['line']}" />
<text x="{x+22}" y="{y+28}" class="mono" font-size="11" letter-spacing="2" fill="{color}">{label}</text>
<text x="{x+22}" y="{y+61}" font-size="25" font-weight="600" fill="{c['text']}">{name}</text>'''
    return wrap('Jack Ou — AI Full-Stack Engineer', 'From database internals to AI products. Three connected layers: products, agent workflows, and systems engineering.', 380, body)

def agenthelm(c):
    body = f'''<rect x="1" y="1" width="1198" height="242" rx="18" fill="{c['bg']}" stroke="{c['line']}" />
<text x="40" y="38" class="mono" font-size="12" letter-spacing="2" fill="{c['accent']}">FEATURED / OPEN SOURCE</text>
<text x="38" y="93" font-size="42" font-weight="700" letter-spacing="-1" fill="{c['text']}">AgentHelm</text>
<text x="40" y="127" font-size="20" fill="{c['muted']}">A local-first workspace for</text>
<text x="40" y="156" font-size="20" fill="{c['muted']}">multi-agent research.</text>
<text x="40" y="207" class="mono" font-size="12" fill="{c['accent']}">CLAUDE CODE + CODEX</text>
<path d="M456 36V208" stroke="{c['line']}" />
<path d="M652 91H710M860 91H912V60H950M912 91V122H950" fill="none" stroke="{c['accent']}" stroke-width="2" />
<circle cx="912" cy="91" r="4" fill="{c['accent']}" />'''
    for x, y, width, height, label in [(500,64,152,54,'Dispatcher'), (710,64,150,54,'Lead'), (950,39,198,43,'Executor'), (950,101,198,43,'Executor')]:
        body += f'''\n<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="9" fill="{c['panel']}" stroke="{c['line']}" />
<text x="{x+width/2}" y="{y+height/2+6}" text-anchor="middle" font-size="17" fill="{c['text']}">{label}</text>'''
    body += f'''\n<path d="M576 118V168M785 118V168M1049 144V168" fill="none" stroke="{c['line']}" stroke-dasharray="4 5" />
<rect x="500" y="168" width="648" height="43" rx="9" fill="{c['wash']}" />
<text x="824" y="195" text-anchor="middle" class="mono" font-size="13" fill="{c['accent']}">SHARED RULES / TASK STATE / MEMORY</text>'''
    return wrap('AgentHelm — multi-agent research workspace', 'A dispatcher coordinates a Lead and executor agents. They share rules, task state, and memory on disk. Supports Claude Code and Codex.', 244, body)

if __name__ == '__main__':
    ASSETS.mkdir(exist_ok=True)
    for theme, colors in THEMES.items():
        for name, render in [('header', header), ('agenthelm', agenthelm)]:
            target = ASSETS / f'{name}-{theme}.svg'
            target.write_text(render(colors), encoding='utf-8')
            print(target.relative_to(ASSETS.parent))
