"""
06_gamer_hack.py - Grey Hack Simulation
Kensei AI Foundations - Semana 07 - Projeto 6

Simulacao educacional de hacking estilo CTF.
Todos os IPs, hosts e vulnerabilidades sao FICTICIOS.
"""

import random
from datetime import datetime
from pathlib import Path

import streamlit as st

# ─── Page Config ─────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Grey Hack // KENSEI Terminal",
    page_icon="💀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── CSS: Matrix Terminal Theme ───────────────────────────────────────────────────
st.markdown(
    """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0d0d0d;
    background-image: radial-gradient(ellipse at top, #001400 0%, #0d0d0d 70%);
}
[data-testid="stSidebar"] { background: #060606; border-right: 1px solid #1a3a1a; }

.main-title {
    font-family: 'Courier New', monospace;
    font-size: 2.2rem;
    font-weight: 900;
    color: #00ff41;
    text-shadow: 0 0 10px #00ff41, 0 0 25px #00aa22;
    letter-spacing: 6px;
    margin-bottom: 0;
}
.sub-title {
    font-family: 'Courier New', monospace;
    color: #006616;
    font-size: 0.75rem;
    letter-spacing: 10px;
    margin-top: 0;
}
.terminal-output {
    background: #050505;
    border: 1px solid #1a3a1a;
    border-radius: 6px;
    padding: 1rem 1.2rem;
    font-family: 'Courier New', monospace;
    font-size: 0.8rem;
    min-height: 380px;
    max-height: 460px;
    overflow-y: auto;
    white-space: pre-wrap;
    line-height: 1.65;
}
.stat-pill {
    display: inline-block;
    background: #060606;
    border: 1px solid #1a3a1a;
    border-radius: 20px;
    padding: 0.3rem 0.9rem;
    font-family: 'Courier New', monospace;
    font-size: 0.78rem;
    color: #00cc33;
    margin: 0.15rem;
}
.host-card {
    background: #060606;
    border: 1px solid #1a2a1a;
    border-radius: 5px;
    padding: 0.6rem 0.9rem;
    font-family: 'Courier New', monospace;
    font-size: 0.75rem;
    color: #006616;
    margin: 0.2rem 0;
}
.host-card.scanned  { border-color: #445500; color: #aacc00; }
.host-card.compromised { border-color: #880000; color: #ff4444; background: #120000; }
.host-card.owned    { border-color: #00ff41; color: #00ff41; background: #001200; }
.mission-card {
    background: #060810;
    border: 1px solid #003366;
    border-radius: 5px;
    padding: 0.85rem 1rem;
    font-family: 'Courier New', monospace;
    font-size: 0.78rem;
    color: #4488cc;
    margin: 0.35rem 0;
}
.mission-card.active    { border-color: #0066ff; color: #66aaff; }
.mission-card.completed { border-color: #00ff41; color: #00cc33; background: #001200; }
.mission-card.locked    { opacity: 0.4; }
.tool-card {
    background: #060606;
    border: 1px solid #222;
    border-radius: 5px;
    padding: 0.65rem 0.9rem;
    font-family: 'Courier New', monospace;
    font-size: 0.76rem;
    color: #555;
    margin: 0.2rem 0;
}
.tool-card.owned  { border-color: #1a3a1a; color: #00cc33; }
.progress-bar-bg  { background: #111; border: 1px solid #1a3a1a; border-radius: 8px; height: 14px; width: 100%; margin: 4px 0; }
.progress-bar-fill{ height: 12px; border-radius: 7px; background: linear-gradient(90deg, #00ff41, #007a1e); }

div[data-testid="stTabs"] button { font-family: 'Courier New', monospace !important; color: #006616 !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color: #00ff41 !important; border-bottom: 2px solid #00ff41 !important; }

.stTextInput input {
    background: #060606 !important;
    color: #00ff41 !important;
    border: 1px solid #1a3a1a !important;
    font-family: 'Courier New', monospace !important;
    font-size: 0.85rem !important;
}
.stTextInput input:focus { border-color: #00ff41 !important; box-shadow: 0 0 6px #00ff41 !important; }
.stButton > button {
    background: #060606 !important;
    color: #00ff41 !important;
    border: 1px solid #1a3a1a !important;
    font-family: 'Courier New', monospace !important;
    font-size: 0.78rem !important;
    border-radius: 4px !important;
}
.stButton > button:hover { background: #001400 !important; border-color: #00ff41 !important; box-shadow: 0 0 8px #00ff41 !important; }
.stButton > button:disabled { opacity: 0.35 !important; cursor: not-allowed !important; }
hr { border-color: #1a3a1a !important; }
p, li { font-family: 'Courier New', monospace; color: #006616; font-size: 0.8rem; }
h1, h2, h3, h4 { font-family: 'Courier New', monospace !important; color: #00ff41 !important; }
.stMetric label { font-family: 'Courier New', monospace !important; color: #006616 !important; font-size: 0.75rem !important; }
.stMetric [data-testid="metric-container"] { color: #00ff41 !important; }
.header-logo-wrap { text-align: right; }
.course-footer {
    margin-top: 1.2rem;
    background: linear-gradient(180deg, #050505 0%, #071108 100%);
    border: 1px solid #1a3a1a;
    border-radius: 8px;
    padding: 1rem 1.1rem;
    font-family: 'Courier New', monospace;
}
.course-footer h4 {
    margin: 0 0 0.45rem 0;
    color: #00ff41 !important;
    letter-spacing: 1px;
}
.course-footer p,
.course-footer li {
    color: #80d88f;
    font-size: 0.78rem;
    margin: 0.2rem 0;
}
.course-footer a {
    color: #58a6ff !important;
    text-decoration: none;
}
.course-footer a:hover {
    text-decoration: underline;
}
</style>
""",
    unsafe_allow_html=True,
)

# ─── Static Game Data ─────────────────────────────────────────────────────────────

NETWORK_HOSTS = [
    {"id": "h01", "ip": "192.168.1.10",  "hostname": "gateway-01",      "os": "Linux 5.15",      "role": "Gateway",       "ports": [22, 80, 443],           "vulns": ["CVE-2024-1001 (SSH Auth Bypass)", "CVE-2023-4412 (HTTP Header Inject)"]},
    {"id": "h02", "ip": "192.168.1.20",  "hostname": "web-srv-prod",     "os": "Ubuntu 22.04",    "role": "Web Server",    "ports": [22, 80, 443, 8080],     "vulns": ["SQLi-2024-001 (Login Form)", "XSS-2024-007 (Search Field)"]},
    {"id": "h03", "ip": "192.168.1.30",  "hostname": "db-mysql-01",      "os": "CentOS 8",        "role": "Database",      "ports": [22, 3306],              "vulns": ["CVE-2024-2233 (MySQL Remote Code Exec)"]},
    {"id": "h04", "ip": "192.168.1.40",  "hostname": "mail-srv",         "os": "Debian 11",       "role": "Mail Server",   "ports": [22, 25, 143, 993],      "vulns": ["CVE-2023-9001 (SMTP Relay Open)", "Postfix Buffer Overflow"]},
    {"id": "h05", "ip": "192.168.1.50",  "hostname": "hr-workstation",   "os": "Windows 11",      "role": "Workstation",   "ports": [135, 445, 3389],        "vulns": ["MS17-010 (EternalBlue)", "CVE-2024-3344 (RDP Pre-Auth)"]},
    {"id": "h06", "ip": "192.168.1.60",  "hostname": "file-srv-01",      "os": "Windows Server",  "role": "File Server",   "ports": [445, 139, 22],          "vulns": ["SMB Null Session", "CVE-2024-1177 (SMBv3 RCE)"]},
    {"id": "h07", "ip": "192.168.1.70",  "hostname": "dev-jenkins",      "os": "Ubuntu 20.04",    "role": "CI/CD",         "ports": [22, 8080, 8443],        "vulns": ["Jenkins Unauthenticated RCE", "CVE-2024-4891 (Groovy Script)"]},
    {"id": "h08", "ip": "192.168.1.80",  "hostname": "vpn-concentrator", "os": "Cisco IOS",       "role": "VPN",           "ports": [22, 443, 1194],         "vulns": ["CVE-2024-5599 (IKEv2 Heap Overflow)"]},
    {"id": "h09", "ip": "192.168.2.10",  "hostname": "dc-ad-01",         "os": "Windows Server",  "role": "Domain Ctrl",   "ports": [53, 88, 389, 445, 3268],"vulns": ["ZeroLogon (CVE-2020-1472)", "PrintNightmare (CVE-2021-34527)"]},
    {"id": "h10", "ip": "192.168.2.20",  "hostname": "backup-srv",       "os": "FreeBSD 13",      "role": "Backup",        "ports": [22, 873, 9200],         "vulns": ["CVE-2023-8801 (rsync Path Traversal)"]},
    {"id": "h11", "ip": "10.0.0.5",      "hostname": "firewall-main",    "os": "pfSense 2.7",     "role": "Firewall",      "ports": [22, 443],               "vulns": ["CVE-2024-9999 (pfSense RCE) [CRITICAL]"]},
    {"id": "h12", "ip": "10.0.0.15",     "hostname": "siem-elk",         "os": "Ubuntu 22.04",    "role": "SIEM",          "ports": [22, 5601, 9200],        "vulns": ["CVE-2024-0001 (Kibana SSRF)"]},
]

ALL_TOOLS = [
    {"id": "nmap",       "name": "nmap",            "desc": "Network scanner: hosts, ports, OS fingerprinting.",            "cost": 0,    "owned": True,  "icon": "🔍"},
    {"id": "hydra",      "name": "hydra",           "desc": "Brute-force login cracker for SSH, FTP, RDP, HTTP.",          "cost": 0,    "owned": True,  "icon": "🐉"},
    {"id": "netcat",     "name": "netcat",          "desc": "TCP/UDP swiss-army knife. Reverse shells & port forwarding.", "cost": 100,  "owned": False, "icon": "🔗"},
    {"id": "sqlmap",     "name": "sqlmap",          "desc": "Automated SQL injection and database takeover tool.",         "cost": 200,  "owned": False, "icon": "💉"},
    {"id": "john",       "name": "john-the-ripper", "desc": "Password hash cracker: MD5, SHA1, NTLM, bcrypt.",            "cost": 300,  "owned": False, "icon": "⚒️"},
    {"id": "wireshark",  "name": "wireshark",       "desc": "Packet capture & analysis. Intercept plaintext traffic.",    "cost": 400,  "owned": False, "icon": "📡"},
    {"id": "metasploit", "name": "metasploit",      "desc": "Exploit framework. Required for advanced RCE modules.",      "cost": 500,  "owned": False, "icon": "🎯"},
    {"id": "mimikatz",   "name": "mimikatz",        "desc": "Windows credential dumper. Extracts hashes from memory.",    "cost": 750,  "owned": False, "icon": "🔑"},
]

MISSIONS_TEMPLATE = [
    {
        "id": "m01", "title": "FIRST CONTACT",    "difficulty": "★☆☆☆☆", "client": "Anonymous",
        "reward_credits": 200, "reward_xp": 150, "status": "available",
        "objective": "Scan the 192.168.1.x subnet and identify at least 5 active hosts.",
        "hint": "Use: nmap 192.168.1.0/24",  "goal": "scan_5",
    },
    {
        "id": "m02", "title": "DATA BREACH",      "difficulty": "★★☆☆☆", "client": "Shadow Broker",
        "reward_credits": 800, "reward_xp": 500, "status": "locked",
        "objective": "Compromise the MySQL database server (192.168.1.30) and extract data.",
        "hint": "Scan db-mysql-01, then exploit CVE-2024-2233. Use: exploit 192.168.1.30 CVE-2024-2233",
        "goal": "compromise_h03",
    },
    {
        "id": "m03", "title": "GHOST PROTOCOL",   "difficulty": "★★★☆☆", "client": "Ghost Cell",
        "reward_credits": 1500, "reward_xp": 1000, "status": "locked",
        "objective": "Compromise the mail server (192.168.1.40) and access the email archive.",
        "hint": "exploit 192.168.1.40 Postfix   (tip: buy metasploit first)",
        "goal": "compromise_h04",
    },
    {
        "id": "m04", "title": "ZERO DAY",         "difficulty": "★★★★☆", "client": "[UNKNOWN]",
        "reward_credits": 3000, "reward_xp": 2500, "status": "locked",
        "objective": "Take control of the Domain Controller (192.168.2.10) via ZeroLogon.",
        "hint": "exploit 192.168.2.10 ZeroLogon  (requires metasploit)",
        "goal": "compromise_h09",
    },
    {
        "id": "m05", "title": "KING OF THE HILL", "difficulty": "★★★★★", "client": "[CLASSIFIED]",
        "reward_credits": 10000, "reward_xp": 8000, "status": "locked",
        "objective": "Own the firewall (10.0.0.5). Become the network.",
        "hint": "exploit 10.0.0.5 CVE-2024-9999  (requires metasploit)",
        "goal": "compromise_h11",
    },
]

SERVICE_MAP = {
    22: "ssh", 25: "smtp", 53: "dns", 80: "http", 88: "kerberos", 135: "msrpc",
    139: "netbios", 143: "imap", 389: "ldap", 443: "https", 445: "smb",
    873: "rsync", 993: "imaps", 1194: "openvpn", 3268: "ldap-gc", 3306: "mysql",
    3389: "rdp", 5601: "kibana", 8080: "http-alt", 8443: "https-alt", 9200: "elasticsearch",
}

LOOT_FILES = {
    "h01": ["/etc/hosts", "/var/log/firewall.log", "/root/.ssh/authorized_keys"],
    "h02": ["/var/www/html/config.php", "/home/deploy/.env", "/var/log/nginx/access.log"],
    "h03": ["/root/mysql_backup.sql", "/etc/mysql/my.cnf", "/home/dbadmin/credentials.txt"],
    "h04": ["/var/mail/ceo/inbox.mbox", "/etc/postfix/sasl_passwd", "/root/email_archive.tar.gz"],
    "h05": ["C:/Users/hradmin/Documents/employees.xlsx", "C:/Users/hradmin/passwords.kdbx"],
    "h06": ["\\\\share\\finance\\Q4_2025_budget.xlsx", "\\\\share\\hr\\employee_db.sql"],
    "h07": ["/var/jenkins_home/credentials.xml", "/root/.jenkins/secrets/master.key"],
    "h08": ["/etc/ipsec.conf", "/etc/ipsec.secrets", "/var/log/vpn.log"],
    "h09": ["C:/Windows/NTDS/ntds.dit", "C:/Windows/SYSVOL/domain/scripts/login.bat"],
    "h10": ["/backup/corp_full_20250501.tar.gz", "/etc/rsyncd.conf"],
    "h11": ["/cf/conf/config.xml", "/var/log/filter.log", "/root/firewall_rules.txt"],
    "h12": ["/etc/elasticsearch/elasticsearch.yml", "/var/log/logstash/logstash.log"],
}

FAKE_PASSWORDS = ["toor", "admin123", "P@ssw0rd!", "kensei2025", "letmein", "Sup3rS3cr3t", "hunter2"]

# ─── Session State Init ───────────────────────────────────────────────────────────


def _add_line(text: str, style: str = "ok"):
    ts = datetime.now().strftime("%H:%M:%S")
    st.session_state.terminal.append({"ts": ts, "text": text, "style": style})
    if len(st.session_state.terminal) > 120:
        st.session_state.terminal = st.session_state.terminal[-120:]


def _add_xp(amount: int):
    p = st.session_state.player
    p["xp"] += amount
    xp_needed = p["level"] * 1000
    if p["xp"] >= xp_needed:
        p["level"] += 1
        p["xp"] -= xp_needed
        _add_line(f"  [★] LEVEL UP! Welcome to Level {p['level']}!", "warn")
        _add_line("", "")


def _add_credits(amount: int):
    st.session_state.player["credits"] += amount


def _check_missions():
    net = st.session_state.network
    mss = st.session_state.missions

    scanned = sum(1 for h in net.values() if h["status"] != "unknown")
    if scanned >= 5 and mss["m01"]["status"] == "available":
        mss["m01"]["status"] = "completed"
        _add_credits(mss["m01"]["reward_credits"])
        _add_xp(mss["m01"]["reward_xp"])
        mss["m02"]["status"] = "available"
        _add_line(f"  [✓] MISSION COMPLETE: {mss['m01']['title']} | +{mss['m01']['reward_credits']}¢ +{mss['m01']['reward_xp']}XP", "warn")

    for mission_id, host_id in [("m02", "h03"), ("m03", "h04"), ("m04", "h09"), ("m05", "h11")]:
        unlock_next = {"m02": "m03", "m03": "m04", "m04": "m05"}.get(mission_id)
        if net.get(host_id, {}).get("status") in ("compromised", "owned") and mss[mission_id]["status"] == "available":
            mss[mission_id]["status"] = "completed"
            _add_credits(mss[mission_id]["reward_credits"])
            _add_xp(mss[mission_id]["reward_xp"])
            if unlock_next:
                mss[unlock_next]["status"] = "available"
            _add_line(f"  [✓] MISSION COMPLETE: {mss[mission_id]['title']} | +{mss[mission_id]['reward_credits']}¢ +{mss[mission_id]['reward_xp']}XP", "warn")
            _add_line("", "")


def init_game():
    if "player" not in st.session_state:
        st.session_state.player = {"name": "ghost_0x00", "level": 1, "xp": 0, "credits": 500, "reputation": 0}

    if "tools" not in st.session_state:
        st.session_state.tools = {t["id"]: dict(t) for t in ALL_TOOLS}

    if "network" not in st.session_state:
        st.session_state.network = {
            h["id"]: {**h, "status": "unknown", "creds": None, "files": list(LOOT_FILES.get(h["id"], []))}
            for h in NETWORK_HOSTS
        }

    if "missions" not in st.session_state:
        st.session_state.missions = {m["id"]: dict(m) for m in MISSIONS_TEMPLATE}

    if "terminal" not in st.session_state:
        st.session_state.terminal = []
        banner = [
            "",
            "   ██████╗ ██████╗ ███████╗██╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗",
            "  ██╔════╝ ██╔══██╗██╔════╝╚██╗ ██╔╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝",
            "  ██║  ███╗██████╔╝█████╗   ╚████╔╝     ███████║███████║██║     █████╔╝ ",
            "  ██║   ██║██╔══██╗██╔══╝    ╚██╔╝      ██╔══██║██╔══██║██║     ██╔═██╗ ",
            "  ╚██████╔╝██║  ██║███████╗   ██║       ██║  ██║██║  ██║╚██████╗██║  ██╗",
            "   ╚═════╝ ╚═╝  ╚═╝╚══════╝   ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝",
            "",
        ]
        for b in banner:
            _add_line(b, "ok")
        _add_line("  KENSEI TERMINAL v3.14.1  //  GREY HACK SIMULATION  //  CTF MODE", "info")
        _add_line("  [!] AVISO: Sistema totalmente ficticio. Apenas para fins educacionais.", "warn")
        _add_line("  [+] VPN conectada: 10.0.0.254 | Jogador: ghost_0x00", "ok")
        _add_line("  [?] Digite 'help' para listar os comandos disponíveis.", "info")
        _add_line("", "")

    if "active_host" not in st.session_state:
        st.session_state.active_host = None


# ─── Command Processor ───────────────────────────────────────────────────────────


def process_command(raw: str):  # noqa: PLR0912, PLR0915 (game logic)
    raw = raw.strip()
    if not raw:
        return
    parts = raw.split()
    cmd = parts[0].lower()
    args = parts[1:]

    net = st.session_state.network
    tools = st.session_state.tools
    player = st.session_state.player

    _add_line(f"  ghost@kensei:~$ {raw}", "cmd")

    # ── help ──────────────────────────────────────────────────────────────────────
    if cmd == "help":
        cmds = [
            ("nmap <ip|range>",          "Escanear hosts, portas, SO e serviços"),
            ("exploit <ip> <vuln>",       "Explorar uma vulnerabilidade"),
            ("crack <ip>",               "Bruteforce SSH/RDP (requer hydra)"),
            ("dump <ip>",                "Extrair hashes do host (requer mimikatz)"),
            ("pivot <ip>",               "Definir host ativo para movimentação lateral"),
            ("ls [ip]",                  "Listar arquivos no host comprometido"),
            ("download <ip> <arquivo>",  "Baixar arquivo do host"),
            ("buy <ferramenta>",         "Comprar ferramenta no mercado negro"),
            ("tools",                    "Listar ferramentas disponíveis"),
            ("missions",                 "Exibir quadro de missões"),
            ("network",                  "Exibir mapa de rede"),
            ("status",                   "Exibir status do jogador"),
            ("clear",                    "Limpar terminal"),
        ]
        _add_line("  COMANDOS DISPONÍVEIS:", "info")
        _add_line("  " + "─" * 58, "info")
        for c, d in cmds:
            _add_line(f"  {c:<30} {d}", "info")
        _add_line("", "")

    # ── clear ─────────────────────────────────────────────────────────────────────
    elif cmd == "clear":
        st.session_state.terminal = []
        _add_line("  [+] Terminal limpo.", "ok")
        _add_line("", "")

    # ── status ────────────────────────────────────────────────────────────────────
    elif cmd == "status":
        p = player
        xp_need = p["level"] * 1000
        owned = sum(1 for h in net.values() if h["status"] in ("compromised", "owned"))
        _add_line(f"  ┌─ JOGADOR: {p['name']}", "ok")
        _add_line(f"  │  Level      : {p['level']}", "ok")
        _add_line(f"  │  XP         : {p['xp']} / {xp_need}", "ok")
        _add_line(f"  │  Credits    : {p['credits']} ¢", "ok")
        _add_line(f"  │  Reputacao  : {p['reputation']}", "ok")
        _add_line(f"  └─ Hosts pwned: {owned}/{len(net)}", "ok")
        _add_line("", "")

    # ── network ───────────────────────────────────────────────────────────────────
    elif cmd == "network":
        _add_line("  TOPOLOGIA DE REDE:", "info")
        _add_line(f"  {'IP':<16} {'Hostname':<22} {'Status':<14} {'OS'}", "info")
        _add_line("  " + "─" * 64, "info")
        for h in net.values():
            icon = {"unknown": "❓", "scanned": "🔍", "compromised": "💀", "owned": "✅"}.get(h["status"], "?")
            sty  = {"unknown": "err", "scanned": "warn", "compromised": "err", "owned": "ok"}.get(h["status"], "ok")
            _add_line(f"  {h['ip']:<16} {h['hostname']:<22} {icon} {h['status']:<12} {h['os']}", sty)
        _add_line("", "")

    # ── missions ──────────────────────────────────────────────────────────────────
    elif cmd == "missions":
        _add_line("  QUADRO DE MISSÕES:", "info")
        _add_line("  " + "─" * 60, "info")
        for m in st.session_state.missions.values():
            icons = {"completed": "✅", "available": "▶️", "locked": "🔒"}
            stys  = {"completed": "ok", "available": "info", "locked": "warn"}
            icon = icons.get(m["status"], "?")
            sty  = stys.get(m["status"], "ok")
            _add_line(f"  [{icon}] {m['title']} {m['difficulty']}  |  +{m['reward_credits']}¢  +{m['reward_xp']}XP", sty)
            if m["status"] in ("available", "completed"):
                _add_line(f"       Obj:  {m['objective']}", sty)
                _add_line(f"       Hint: {m['hint']}", "warn")
            _add_line("", "")

    # ── tools ─────────────────────────────────────────────────────────────────────
    elif cmd == "tools":
        _add_line("  FERRAMENTAS:", "info")
        for t in tools.values():
            if t["owned"]:
                _add_line(f"  [✅] {t['icon']} {t['name']:<22} {t['desc']}", "ok")
            else:
                _add_line(f"  [🔒] {t['icon']} {t['name']:<22} {t['desc']}  |  {t['cost']}¢", "warn")
        _add_line("", "")

    # ── buy <tool> ────────────────────────────────────────────────────────────────
    elif cmd == "buy":
        if not args:
            _add_line("  [!] Uso: buy <ferramenta>", "err")
        else:
            tid = args[0].lower()
            if tid not in tools:
                _add_line(f"  [✗] Ferramenta desconhecida: {tid}", "err")
            elif tools[tid]["owned"]:
                _add_line(f"  [!] Você já possui {tid}.", "warn")
            elif player["credits"] < tools[tid]["cost"]:
                _add_line(f"  [✗] Créditos insuficientes. Precisa: {tools[tid]['cost']}¢ | Saldo: {player['credits']}¢", "err")
            else:
                player["credits"] -= tools[tid]["cost"]
                tools[tid]["owned"] = True
                _add_line(f"  [+] Adquirido: {tools[tid]['icon']} {tid}  |  -{tools[tid]['cost']}¢", "ok")
        _add_line("", "")

    # ── nmap <ip|range> ───────────────────────────────────────────────────────────
    elif cmd == "nmap":
        if not args:
            _add_line("  [!] Uso: nmap <ip>  ou  nmap 192.168.1.0/24", "err")
        else:
            target = args[0]
            if "/" in target:
                subnet = target.split("/")[0].rsplit(".", 1)[0]
                matches = [h for h in net.values() if h["ip"].startswith(subnet)]
                _add_line(f"  [*] Iniciando Nmap em {target} ...", "ok")
                if not matches:
                    _add_line(f"  [0] Nenhum host encontrado em {target}.", "err")
                else:
                    for h in matches:
                        if h["status"] == "unknown":
                            h["status"] = "scanned"
                            _add_xp(20)
                        ports_str = ", ".join(str(p) for p in h["ports"])
                        _add_line(f"  Host up: {h['hostname']} ({h['ip']})  OS: {h['os']}  Portas: {ports_str}", "ok")
                    _add_line(f"  [+] {len(matches)} hosts ativos em {target}", "ok")
                    _check_missions()
            else:
                host = next((h for h in net.values() if h["ip"] == target), None)
                if not host:
                    _add_line(f"  [!] {target}: host inacessível ou filtrado.", "err")
                else:
                    if host["status"] == "unknown":
                        host["status"] = "scanned"
                        _add_xp(20)
                    _add_line(f"  Nmap scan report for {host['hostname']} ({host['ip']})", "ok")
                    _add_line(f"  Host up.  SO: {host['os']}", "ok")
                    _add_line(f"  {'PORTA':<8} {'ESTADO':<8} SERVIÇO", "info")
                    for p in host["ports"]:
                        svc = SERVICE_MAP.get(p, "unknown")
                        _add_line(f"  {p}/tcp  {'open':<8} {svc}", "ok")
                    if host["status"] != "unknown":
                        _add_line(f"  [*] Vulnerabilidades detectadas:", "warn")
                        for v in host["vulns"]:
                            _add_line(f"      ⚠️  {v}", "warn")
                    _check_missions()
        _add_line("", "")

    # ── exploit <ip> <vuln_keyword> ───────────────────────────────────────────────
    elif cmd == "exploit":
        if len(args) < 2:
            _add_line("  [!] Uso: exploit <ip> <palavra-chave-da-vuln>", "err")
            _add_line("  [!] Ex:  exploit 192.168.1.20 SQLi-2024-001", "err")
        else:
            target_ip = args[0]
            vuln_kw = " ".join(args[1:]).lower()
            host = next((h for h in net.values() if h["ip"] == target_ip), None)

            if not host:
                _add_line(f"  [✗] Sem rota para {target_ip}.", "err")
            elif host["status"] == "unknown":
                _add_line(f"  [!] Escaneie o alvo primeiro: nmap {target_ip}", "warn")
            elif host["status"] in ("compromised", "owned"):
                _add_line(f"  [!] {host['hostname']} já está comprometido.", "warn")
            else:
                matched = next((v for v in host["vulns"] if vuln_kw in v.lower()), None)
                if not matched:
                    _add_line(f"  [✗] Vuln '{' '.join(args[1:])}' não encontrada em {host['hostname']}.", "err")
                    _add_line(f"  [?] Vulns conhecidas: {', '.join(host['vulns'])}", "warn")
                else:
                    needs_meta = any(k in matched for k in ["RCE", "Heap", "EternalBlue", "ZeroLogon", "PrintNightmare", "pfSense"])
                    if needs_meta and not tools.get("metasploit", {}).get("owned"):
                        _add_line(f"  [!] Este exploit requer Metasploit.", "warn")
                        _add_line(f"  [!] Compre com: buy metasploit  (500¢)", "warn")
                    else:
                        _add_line(f"  [*] Carregando módulo: {matched}", "ok")
                        _add_line(f"  [*] Alvo: {host['ip']} ({host['hostname']})", "ok")
                        _add_line(f"  [*] Executando payload...", "ok")
                        chance = 0.80 if tools.get("metasploit", {}).get("owned") else 0.55
                        if random.random() < chance:
                            host["status"] = "compromised"
                            host["creds"] = f"root:{random.choice(FAKE_PASSWORDS)}"
                            _add_line(f"  [✓] SHELL OBTIDO! {host['hostname']} comprometido!", "ok")
                            _add_line(f"  [+] Credenciais: {host['creds']}", "data")
                            _add_line(f"  [+] root@{host['hostname']}:~# ", "ok")
                            _add_xp(random.randint(100, 350))
                            _add_credits(random.randint(50, 250))
                        else:
                            _add_line(f"  [✗] Exploit falhou. IDS pode ter detectado.", "err")
                            _add_line(f"  [!] Tente outro vetor ou aguarde.", "warn")
                _check_missions()
        _add_line("", "")

    # ── crack <ip> ────────────────────────────────────────────────────────────────
    elif cmd == "crack":
        if not args:
            _add_line("  [!] Uso: crack <ip>", "err")
        else:
            target_ip = args[0]
            host = next((h for h in net.values() if h["ip"] == target_ip), None)
            if not host:
                _add_line(f"  [✗] Sem rota para {target_ip}.", "err")
            elif not tools.get("hydra", {}).get("owned"):
                _add_line(f"  [!] Hydra necessário para bruteforce.", "err")
            elif host["status"] == "unknown":
                _add_line(f"  [!] Escaneie primeiro: nmap {target_ip}", "warn")
            elif not any(p in host["ports"] for p in (22, 3389)):
                _add_line(f"  [!] Nenhuma porta SSH/RDP aberta em {host['hostname']}.", "err")
            else:
                wordlist = FAKE_PASSWORDS[:4]
                _add_line(f"  [*] Hydra brute-force em {host['ip']} ...", "ok")
                _add_line(f"  [*] Testando {len(wordlist)} senhas ...", "ok")
                if random.random() < 0.65:
                    pw = random.choice(wordlist)
                    _add_line(f"  [✓] Senha encontrada: admin:{pw}", "ok")
                    if not host["creds"]:
                        host["creds"] = f"admin:{pw}"
                    _add_xp(50)
                else:
                    _add_line(f"  [✗] Bruteforce falhou. Senha não está na wordlist.", "err")
                    _add_line(f"  [!] Tente com john e uma wordlist maior.", "warn")
        _add_line("", "")

    # ── dump <ip> ─────────────────────────────────────────────────────────────────
    elif cmd == "dump":
        if not args:
            _add_line("  [!] Uso: dump <ip>", "err")
        else:
            target_ip = args[0]
            host = next((h for h in net.values() if h["ip"] == target_ip), None)
            if not host:
                _add_line(f"  [✗] Sem rota para {target_ip}.", "err")
            elif not tools.get("mimikatz", {}).get("owned"):
                _add_line(f"  [!] Mimikatz necessário. Compre: buy mimikatz  (750¢)", "warn")
            elif host["status"] not in ("compromised", "owned"):
                _add_line(f"  [!] Host ainda não comprometido.", "warn")
            else:
                _add_line(f"  [*] Executando mimikatz em {host['hostname']} ...", "ok")
                users = ["admin", "backupadm", "svcuser"]
                for u in users:
                    h_val = f"{random.randint(10000,99999):x}:{random.randint(100000,999999):x}"
                    _add_line(f"  [+] {u}: NTLM:{h_val}", "data")
                _add_line(f"  [✓] Credenciais extraídas. Use john para crackear os hashes.", "ok")
                _add_xp(60)
        _add_line("", "")

    # ── pivot <ip> ────────────────────────────────────────────────────────────────
    elif cmd == "pivot":
        if not args:
            _add_line("  [!] Uso: pivot <ip>", "err")
        else:
            target_ip = args[0]
            host = next((h for h in net.values() if h["ip"] == target_ip), None)
            if not host:
                _add_line(f"  [✗] Sem rota para {target_ip}.", "err")
            elif host["status"] not in ("compromised", "owned"):
                _add_line(f"  [!] {target_ip} ainda não comprometido.", "warn")
            else:
                st.session_state.active_host = host
                host["status"] = "owned"
                _add_line(f"  [✓] Pivotando para {host['hostname']} ({host['ip']})", "ok")
                _add_line(f"  root@{host['hostname']}:~# ", "ok")
                _add_xp(30)
        _add_line("", "")

    # ── ls [ip] ───────────────────────────────────────────────────────────────────
    elif cmd == "ls":
        tip = args[0] if args else (st.session_state.active_host["ip"] if st.session_state.active_host else None)
        if not tip:
            _add_line("  [!] Uso: ls <ip>  ou faça pivot em um host primeiro.", "err")
        else:
            host = next((h for h in net.values() if h["ip"] == tip), None)
            if not host or host["status"] not in ("compromised", "owned"):
                _add_line(f"  [!] Não conectado a {tip}.", "err")
            else:
                _add_line(f"  root@{host['hostname']}:/# ls -la", "ok")
                for f in host.get("files", []):
                    size = random.randint(512, 99999)
                    _add_line(f"  -rw-r--r-- 1 root root {size:>8}  {f}", "ok")
        _add_line("", "")

    # ── download <ip> <arquivo> ───────────────────────────────────────────────────
    elif cmd == "download":
        if len(args) < 2:
            _add_line("  [!] Uso: download <ip> <arquivo>", "err")
        else:
            tip = args[0]
            fname = args[1]
            host = next((h for h in net.values() if h["ip"] == tip), None)
            if not host or host["status"] not in ("compromised", "owned"):
                _add_line(f"  [!] Não conectado a {tip}.", "err")
            else:
                size = random.uniform(0.5, 42.0)
                _add_line(f"  [*] Baixando {fname} de {host['hostname']} ...", "ok")
                _add_line(f"  [+] Transferência concluída. {size:.1f}KB recebidos.", "ok")
                _add_line(f"  [+] Arquivo salvo em: ~/loot/{fname.split('/')[-1]}", "data")
                _add_xp(30)
                _add_credits(50)
        _add_line("", "")

    # ── unknown command ───────────────────────────────────────────────────────────
    else:
        _add_line(f"  [✗] Comando não encontrado: '{cmd}'. Digite 'help'.", "err")
        _add_line("", "")


# ─── Game Init ────────────────────────────────────────────────────────────────────
init_game()
LOGO_PATH = Path(__file__).resolve().parents[1] / "img" / "logo_kensei.png"

# ─── Header ───────────────────────────────────────────────────────────────────────
header_left, header_right = st.columns([4, 2])
with header_left:
    st.markdown('<div class="main-title">💀 GREY HACK // KENSEI TERMINAL</div>', unsafe_allow_html=True)
with header_right:
    st.markdown('<div class="header-logo-wrap">', unsafe_allow_html=True)
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=280)
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">SIMULAÇÃO FICTÍCIA DE HACKING  //  APENAS PARA FINS EDUCACIONAIS</div>', unsafe_allow_html=True)
st.divider()

# ─── Stats Bar ────────────────────────────────────────────────────────────────────
p = st.session_state.player
xp_need = p["level"] * 1000
xp_pct = int((p["xp"] / xp_need) * 100) if xp_need else 0

cs1, cs2, cs3, cs4, cs5 = st.columns([2, 1, 1, 1, 3])
with cs1:
    st.markdown(f'<span class="stat-pill">👤 {p["name"]}</span>', unsafe_allow_html=True)
with cs2:
    st.markdown(f'<span class="stat-pill">⭐ LVL {p["level"]}</span>', unsafe_allow_html=True)
with cs3:
    st.markdown(f'<span class="stat-pill" style="color:#ffdd00">💰 {p["credits"]}¢</span>', unsafe_allow_html=True)
with cs4:
    st.markdown(f'<span class="stat-pill" style="color:#aa66ff">🔮 {p["xp"]}/{xp_need} XP</span>', unsafe_allow_html=True)
with cs5:
    st.markdown(
        f'<div class="progress-bar-bg"><div class="progress-bar-fill" style="width:{xp_pct}%"></div></div>',
        unsafe_allow_html=True,
    )

st.divider()

# ─── Tabs ─────────────────────────────────────────────────────────────────────────
tab_term, tab_net, tab_mis, tab_kit, tab_brief = st.tabs(
    ["🖥️ Terminal", "🗺️ Network", "📋 Missions", "🔧 Toolkit", "📄 Briefing"]
)

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 1 — TERMINAL
# ══════════════════════════════════════════════════════════════════════════════════
with tab_term:
    COLOR_MAP = {
        "ok": "#00ff41", "err": "#ff4444", "warn": "#ffaa00",
        "info": "#44aaff", "data": "#cc44ff", "cmd": "#ffffff", "": "#006616",
    }
    html_lines = ""
    for line in st.session_state.terminal:
        color = COLOR_MAP.get(line.get("style", ""), "#00cc33")
        text = line["text"].replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        html_lines += f'<span style="color:{color}">{text}</span>\n'

    st.markdown(f'<div class="terminal-output">{html_lines}</div>', unsafe_allow_html=True)

    col_inp, col_run = st.columns([7, 1])
    with col_inp:
        user_cmd = st.text_input(
            "cmd",
            key="cmd_input",
            placeholder="ghost@kensei:~$ digite um comando...",
            label_visibility="collapsed",
        )
    with col_run:
        run_btn = st.button("▶ RUN", use_container_width=True)

    if run_btn and user_cmd:
        process_command(user_cmd)
        st.rerun()

    st.markdown("**Atalhos rápidos:**")
    qcols = st.columns(7)
    quick = [
        ("🔍 Scan LAN",  "nmap 192.168.1.0/24"),
        ("🔍 Scan DMZ",  "nmap 10.0.0.0/24"),
        ("🔍 Scan Corp", "nmap 192.168.2.0/24"),
        ("📋 Missões",   "missions"),
        ("🔧 Tools",     "tools"),
        ("📊 Status",    "status"),
        ("🗑️ Clear",     "clear"),
    ]
    for i, (label, qcmd) in enumerate(quick):
        with qcols[i]:
            if st.button(label, use_container_width=True, key=f"q_{i}"):
                process_command(qcmd)
                st.rerun()

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 2 — NETWORK MAP
# ══════════════════════════════════════════════════════════════════════════════════
with tab_net:
    net = st.session_state.network
    status_counts = {s: sum(1 for h in net.values() if h["status"] == s) for s in ("unknown", "scanned", "compromised", "owned")}

    mc1, mc2, mc3, mc4 = st.columns(4)
    mc1.metric("❓ Desconhecido", status_counts["unknown"])
    mc2.metric("🔍 Escaneado",    status_counts["scanned"])
    mc3.metric("💀 Comprometido", status_counts["compromised"])
    mc4.metric("✅ Controlado",   status_counts["owned"])

    st.divider()
    col_list, col_detail = st.columns([1, 2])

    with col_list:
        st.markdown("**🗺️ Hosts na Rede**")
        for h in net.values():
            css = {"unknown": "host-card", "scanned": "host-card scanned", "compromised": "host-card compromised", "owned": "host-card owned"}.get(h["status"], "host-card")
            icon = {"unknown": "❓", "scanned": "🔍", "compromised": "💀", "owned": "✅"}.get(h["status"], "?")
            ports_str = ", ".join(str(pp) for pp in h["ports"])
            st.markdown(
                f'<div class="{css}"><b>{icon} {h["hostname"]}</b><br>'
                f'<span style="font-size:0.7rem">{h["ip"]} | {h["os"]}<br>Portas: {ports_str}</span></div>',
                unsafe_allow_html=True,
            )

    with col_detail:
        st.markdown("**🎯 Detalhes do Alvo**")
        all_ips = [h["ip"] for h in net.values()]
        sel_ip = st.selectbox("Selecione um host:", all_ips, key="net_sel")

        if sel_ip:
            h = next(hh for hh in net.values() if hh["ip"] == sel_ip)
            vuln_html = ("<br>".join(f"  ⚠️ {v}" for v in h["vulns"])) if h["status"] != "unknown" else "🔒 Escaneie para revelar vulnerabilidades."
            creds_html = f"<br>🔑 Credenciais: <b>{h['creds']}</b>" if h.get("creds") else ""
            files_html = f"<br>📁 Arquivos:<br>{'<br>'.join(h.get('files', []))}" if h.get("files") and h["status"] in ("compromised", "owned") else ""
            css = {"unknown": "host-card", "scanned": "host-card scanned", "compromised": "host-card compromised", "owned": "host-card owned"}.get(h["status"], "host-card")
            st.markdown(
                f'<div class="{css}" style="font-size:0.8rem">'
                f'<b>{h["hostname"]}</b>  ({h["ip"]})<br><br>'
                f'SO: {h["os"]}<br>Papel: {h["role"]}<br>Status: <b>{h["status"].upper()}</b><br>'
                f'Portas: {", ".join(str(pp) for pp in h["ports"])}<br><br>'
                f'{vuln_html}{creds_html}{files_html}</div>',
                unsafe_allow_html=True,
            )

            a1, a2, a3 = st.columns(3)
            with a1:
                if st.button(f"🔍 nmap {h['ip']}", key="na_scan"):
                    process_command(f"nmap {h['ip']}")
                    st.rerun()
            with a2:
                if h["status"] == "scanned" and h["vulns"]:
                    kw = h["vulns"][0].split(" ")[0]
                    if st.button("💉 exploit", key="na_exp"):
                        process_command(f"exploit {h['ip']} {kw}")
                        st.rerun()
            with a3:
                if h["status"] in ("compromised", "owned"):
                    if st.button(f"📁 ls", key="na_ls"):
                        process_command(f"ls {h['ip']}")
                        st.rerun()

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 3 — MISSIONS
# ══════════════════════════════════════════════════════════════════════════════════
with tab_mis:
    mss = st.session_state.missions
    cc, ca, cl = (
        sum(1 for m in mss.values() if m["status"] == s)
        for s in ("completed", "available", "locked")
    )
    mc1, mc2, mc3 = st.columns(3)
    mc1.metric("✅ Concluídas", cc)
    mc2.metric("▶️ Disponíveis", ca)
    mc3.metric("🔒 Bloqueadas",  cl)
    st.divider()

    for m in mss.values():
        css = {"completed": "mission-card completed", "available": "mission-card active", "locked": "mission-card locked"}.get(m["status"], "mission-card")
        badge = {"completed": "✅ CONCLUÍDA", "available": "▶️ ATIVA", "locked": "🔒 BLOQUEADA"}.get(m["status"], "")
        hint_html = f"<br><b>Hint:</b> <code>{m['hint']}</code>" if m["status"] in ("available", "completed") else ""
        st.markdown(
            f'<div class="{css}">'
            f'<b>{m["title"]}</b> {m["difficulty"]} &nbsp;<small>{badge}</small><br>'
            f'<small>Cliente: {m["client"]}  |  Recompensa: +{m["reward_credits"]}¢ / +{m["reward_xp"]}XP</small><br><br>'
            f'<b>Objetivo:</b> {m["objective"]}{hint_html}</div>',
            unsafe_allow_html=True,
        )

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 4 — TOOLKIT
# ══════════════════════════════════════════════════════════════════════════════════
with tab_kit:
    tools = st.session_state.tools
    p = st.session_state.player
    col_t1, col_t2 = st.columns([3, 1])

    with col_t1:
        st.markdown("**🔧 Arsenal de Ferramentas**")
        for tool in tools.values():
            css = "tool-card owned" if tool["owned"] else "tool-card"
            status_txt = "✅ POSSUÍDO" if tool["owned"] else f"🔒  {tool['cost']}¢"
            col_ti, col_tb = st.columns([5, 1])
            with col_ti:
                st.markdown(
                    f'<div class="{css}"><b>{tool["icon"]} {tool["name"]}</b>  <small>{status_txt}</small><br>'
                    f'<small>{tool["desc"]}</small></div>',
                    unsafe_allow_html=True,
                )
            with col_tb:
                if not tool["owned"]:
                    disabled = p["credits"] < tool["cost"]
                    if st.button("Comprar", key=f"buy_{tool['id']}", disabled=disabled):
                        process_command(f"buy {tool['id']}")
                        st.rerun()

    with col_t2:
        st.markdown("**💰 Saldo**")
        st.markdown(f'<span class="stat-pill" style="font-size:1.1rem; color:#ffdd00">💰 {p["credits"]}¢</span>', unsafe_allow_html=True)
        st.divider()
        st.markdown("""
**Estratégia de compra:**

1. `netcat` — reverse shells básicos
2. `sqlmap` — web apps
3. `john` — crackear hashes  
4. `wireshark` — interceptar tráfego
5. `metasploit` — RCE avançado ⚡
6. `mimikatz` — dump de credenciais
""")

# ══════════════════════════════════════════════════════════════════════════════════
# TAB 5 — BRIEFING
# ══════════════════════════════════════════════════════════════════════════════════
with tab_brief:
    st.markdown("""
## 📄 BRIEFING DA OPERAÇÃO

**[CLASSIFICADO - SOMENTE PARA SEUS OLHOS]**

Você foi contratado para um **red team simulado** em uma rede corporativa fictícia.
Este é um jogo estilo **CTF (Capture The Flag)** inspirado no Grey Hack.

---

### 🎯 Missões

| Missão | Dificuldade | Alvo | Recompensa |
|--------|-------------|------|------------|
| FIRST CONTACT    | ★☆☆☆☆ | Rede 192.168.1.x    | 200¢  |
| DATA BREACH      | ★★☆☆☆ | db-mysql-01 (.1.30) | 800¢  |
| GHOST PROTOCOL   | ★★★☆☆ | mail-srv (.1.40)    | 1.500¢|
| ZERO DAY         | ★★★★☆ | dc-ad-01 (.2.10)    | 3.000¢|
| KING OF THE HILL | ★★★★★ | firewall (10.0.0.5) | 10.000¢|

---

### 🗺️ Topologia da Rede

```
INTERNET
    │
    ▼
[Firewall: 10.0.0.5]  ← Missão 5: KING OF THE HILL
    │
    ├── [SIEM: 10.0.0.15]  (monitoramento)
    │
    ├── SUBNET DMZ: 192.168.1.x
    │       ├── gateway-01      (.10)
    │       ├── web-srv-prod    (.20)  ← SQLi vulnerability
    │       ├── db-mysql-01     (.30)  ← Missão 2: DATA BREACH
    │       ├── mail-srv        (.40)  ← Missão 3: GHOST PROTOCOL
    │       ├── hr-workstation  (.50)  ← EternalBlue (MS17-010)
    │       ├── file-srv-01     (.60)  ← SMB vulnerabilities
    │       ├── dev-jenkins     (.70)  ← CI/CD unauthenticated RCE
    │       └── vpn-concentrator(.80)
    │
    └── SUBNET CORP: 192.168.2.x
            ├── dc-ad-01   (.10)  ← Missão 4: ZERO DAY
            └── backup-srv (.20)
```

---

### 📚 Referência de Comandos

| Comando | Descrição |
|---------|-----------|
| `nmap 192.168.1.0/24` | Escanear subnet inteira |
| `nmap 192.168.1.30` | Scan detalhado de um host |
| `exploit 192.168.1.30 CVE-2024-2233` | Explorar vuln específica |
| `crack 192.168.1.20` | Bruteforce SSH/RDP |
| `dump 192.168.1.20` | Extrair hashes (mimikatz) |
| `pivot 192.168.1.20` | Definir shell ativa |
| `ls 192.168.1.20` | Listar arquivos no host |
| `download 192.168.1.20 /etc/passwd` | Baixar arquivo |
| `buy metasploit` | Comprar ferramenta (500¢) |

---

### 💡 Dicas de Progresso

1. **Comece** com `nmap 192.168.1.0/24` para completar a Missão 1
2. **Compre metasploit** assim que tiver 500¢ — desbloqueará muitos exploits
3. **Pivote** nos hosts comprometidos para acesso persistente
4. Hosts com **portas 22/3389** abertas podem ser brute-forced com hydra
5. Após comprometer um host, use `ls` e `download` para coletar loot

---

### ⚠️ Aviso Legal

Este é um **jogo de simulação completamente fictício** para educação em cibersegurança.
Todos os IPs, hostnames, vulnerabilidades e exploits foram **inventados para gameplay**.
Nenhum sistema real é alvo ou comprometido nesta simulação.

*Kensei AI Foundations — Semana 7 — Projeto 6*
""")

st.divider()
st.markdown(
        """
<div class="course-footer">
    <h4>Repositorio Principal | Kensei AI Foundations</h4>
    <p>Curso pratico de 8 semanas com foco em IA, dados, automacao e cybersecurity, construindo portfolio real com Python, n8n e Streamlit.</p>
    <ul>
        <li><b>Trilha:</b> Python do zero, analise de dados, APIs de IA, agentes n8n e apps web.</li>
        <li><b>Semana 7:</b> dashboards, chatbot com Gemini, analisador de PDF, SOC com webhook e game CTF.</li>
        <li><b>Repositorio principal:</b> consulte o arquivo README.md na raiz do projeto.</li>
        <li><b>Material da semana:</b> consulte semana-07/README.md para os detalhes dos projetos.</li>
    </ul>
</div>
""",
        unsafe_allow_html=True,
)
