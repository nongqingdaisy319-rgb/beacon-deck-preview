with open('/Users/nongqing/.openclaw/workspace/beacon-deck/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Hero
    ('Ask <span class="accent">Beacon</span>. Trade smarter. Earn more.',
     '<span class="accent">Beacon</span> is always on. Working for you.'),
    # Demo section
    ('See What <span translate="no" style="white-space:nowrap">BitMart AI</span> Can Do',
     'See <span translate="no" style="white-space:nowrap">Beacon</span> in Action'),
    ('Ask market questions, get instant answers, and stay ahead — all in your channels.',
     'Market insights, strategy analysis, trade execution — tell Beacon what to do, and it gets it done'),
    # Features section title
    ('Connect Once. Unlock Everything.',
     'Beacon Works. You Earn.'),
    # Feature cards
    ('Never Miss a Move', 'Market Insights'),
    ('While you sleep, Beacon watches the market. Signals, anomalies, and opportunities — delivered before you even check.',
     'Beacon monitors markets in real time — explaining what happened, why it moved, and what to watch next'),
    ('Beat the Market', 'Strategy Analysis'),
    ('BTC whale moves, ETH funding spikes, token unlocks. Beacon surfaces what matters before the crowd reacts.',
     'Share your idea with Beacon, and it runs historical data, finds the gaps, and refines the parameters for you'),
    ('Clear Reports, Zero Noise', 'Portfolio Management'),
    ('No walls of data. Beacon breaks down market analysis into clear, structured summaries — right inside your channels.',
     'Beacon tracks your account at all times — proactively flagging risks and opportunities so you never have to'),
    ('Your 24/7 Crypto Analyst', 'Signal Capture'),
    ('"What\'s driving BTC down?" "How\'s my portfolio?" Just ask Beacon. Real answers in seconds.',
     'Whale movements, funding rate spikes, token unlocks — Beacon monitors 24/7 and pushes critical signals to you'),
    ('Where You Work, It Works', 'Execution Support'),
    ('Web, Desktop, and App. Beacon lives in your channels — not another tab you forget to open.',
     'From strategy to order placement, Beacon walks you through every step. You just confirm'),
    ('Calm Under Volatility', 'OpenClaw Extension'),
    ('When the market moves fast, Beacon gives you context, not just noise. Know what\'s happening and why.',
     'Connect OpenClaw to unlock more Agent capabilities and build your own custom crypto workflows'),
    # How it works
    ('Start in Seconds', 'Up and Running in 30 Seconds'),
    ('Open BitMart AI', 'Open BitMart AI'),
    ('Log in to BitMart and open the AI panel — free for all users.',
     'Log into BitMart and open the AI panel — no setup required'),
    ('Ask Anything', 'Just Start Talking'),
    ('Type your question — market moves, crypto news, or account queries.',
     'Market moves, news, account status — say what\'s on your mind, Beacon understands'),
    ('Act on Insights', 'Get Personalized Answers'),
    ('Get clear answers, follow up, and stay one step ahead of the market.',
     'Based on your account and preferences, Beacon gives answers tailored to you — not just generic replies'),
    # CTA
    ('Beacon is ready when you are.', 'With Beacon on watch, you can sleep easy'),
    ('Your AI, always on. Start a conversation.', 'Always on, always working — your personal crypto AI'),
    # Buttons
    ('>Try Beacon →<', '>Try Beacon →<'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('/Users/nongqing/.openclaw/workspace/beacon-deck/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
