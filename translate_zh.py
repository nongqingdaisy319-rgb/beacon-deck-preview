with open('/Users/nongqing/.openclaw/workspace/beacon-deck/index-zh.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('Capabilities', '核心能力'),
    ('Connect Once. Unlock Everything.', '接入一次，解锁全部。'),
    ('Never Miss a Move', '永不错过行情'),
    ('While you sleep, Beacon watches the market. Signals, anomalies, and opportunities — delivered before you even check.', '你睡着的时候，Beacon 在盯盘。信号、异动、机会 —— 推到你的频道，比你醒来更早。'),
    ('Beat the Market', '先于市场一步'),
    ('BTC whale moves, ETH funding spikes, token unlocks. Beacon surfaces what matters before the crowd reacts.', 'BTC 大户动向、ETH 资金费率异常、代币解锁 —— Beacon 帮你在人群反应之前看到关键信息。'),
    ('Clear Reports, Zero Noise', '报告清晰，零废话'),
    ('No walls of data. Beacon breaks down market analysis into clear, structured summaries — right inside your channels.', '不是一堆数据图表。Beacon 把市场分析整理成结构清晰的摘要，直接出现在你的频道里。'),
    ('Your 24/7 Crypto Analyst', '你的 24 小时加密分析师'),
    ('"What\'s driving BTC down?" "How\'s my portfolio?" Just ask Beacon. Real answers in seconds.', '"BTC 今天为什么跌？""我的持仓现在怎么样？" 直接问 Beacon，几秒内给出真实答案。'),
    ('Where You Work, It Works', '你在哪，它就在哪'),
    ('Web, Desktop, App. Beacon lives in your channels — not another tab you forget to open.', '网页版、桌面端、App 三端同步。Beacon 住在你的频道里 —— 不是那个你总忘了打开的标签页。'),
    ('Calm Under Volatility', '波动时保持清醒'),
    ("When the market moves fast, Beacon gives you context, not just noise. Know what's happening and why.", '行情急速变化时，Beacon 给你的是上下文和判断依据，而不是噪音。知道发生了什么，以及为什么。'),
    ('How It Works', '如何开始'),
    ('Start in Seconds', '30 秒上手'),
    ('Open BitMart AI', '打开 BitMart AI'),
    ('Log in to BitMart and open the AI panel — free for all users.', '登录 BitMart，打开 AI 面板 —— 所有用户免费使用。'),
    ('Ask Anything', '随便问'),
    ('Type your question — market moves, crypto news, or account queries.', '直接输入你的问题 —— 行情动向、加密新闻、账户查询，什么都行。'),
    ('Act on Insights', '据此行动'),
    ('Get clear answers, follow up, and stay one step ahead of the market.', '获得清晰答案，追问细节，比市场快一步。'),
    ('Beacon is ready when you are.', 'Beacon 随时待命。'),
    ('Your AI, always on. Start a conversation.', '你的 AI 助手，全天候在线。开始对话吧。'),
    ('>Try Beacon →<', '>立即体验 →<'),
    ('>Try Beacon<', '>立即体验<'),
    ('<html lang="en" translate="no">', '<html lang="zh-CN">'),
    ('Live Preview', '产品预览'),
    ("Ask market questions, get instant answers, and stay ahead — all in your channels.", '问行情、问策略、问持仓 —— 直接在频道里问，秒出答案。'),
    ('See What <span translate="no" style="white-space:nowrap">BitMart AI</span> Can Do', '看看 <span translate="no" style="white-space:nowrap">BitMart AI</span> 能做什么'),
]

for old, new in replacements:
    content = content.replace(old, new)

with open('/Users/nongqing/.openclaw/workspace/beacon-deck/index-zh.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('done')
