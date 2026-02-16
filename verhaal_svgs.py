# SVG illustrations for each verhaal - both card (360x180) and hero (720x240) versions

SVGS = {
    "waar-switcht-je-klant-van-weg": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Four forces diagram -->
            <circle cx="180" cy="90" r="28" stroke="#D97706" stroke-width="2" fill="none"/>
            <text x="180" y="94" text-anchor="middle" font-family="DM Sans" font-size="11" fill="#D97706" font-weight="600">?</text>
            <!-- Push arrow left -->
            <line x1="60" y1="90" x2="140" y2="90" stroke="#44403C" stroke-width="2"/>
            <polygon points="140,84 152,90 140,96" fill="#44403C"/>
            <text x="60" y="78" font-family="DM Sans" font-size="10" fill="#78716C">Verschuiving</text>
            <!-- Pull arrow right -->
            <line x1="208" y1="90" x2="300" y2="90" stroke="#44403C" stroke-width="2"/>
            <polygon points="300,84 312,90 300,96" fill="#44403C"/>
            <text x="260" y="78" font-family="DM Sans" font-size="10" fill="#78716C">Propositie</text>
            <!-- Friction up -->
            <line x1="180" y1="52" x2="180" y2="30" stroke="#A8A29E" stroke-width="1.5" stroke-dasharray="4 3"/>
            <text x="180" y="22" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#A8A29E">Frictie</text>
            <!-- Habit down -->
            <line x1="180" y1="128" x2="180" y2="150" stroke="#A8A29E" stroke-width="1.5" stroke-dasharray="4 3"/>
            <text x="180" y="168" text-anchor="middle" font-family="DM Sans" font-size="10" fill="#A8A29E">Gewoonte</text>
        </svg>''',
    },
    "waarom-klanten-echt-overstappen": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Customer Forces quadrant -->
            <!-- Crosshair -->
            <line x1="180" y1="30" x2="180" y2="150" stroke="#D6D3D1" stroke-width="1"/>
            <line x1="60" y1="90" x2="300" y2="90" stroke="#D6D3D1" stroke-width="1"/>
            <!-- Push arrow -->
            <line x1="100" y1="90" x2="160" y2="90" stroke="#D97706" stroke-width="2.5"/>
            <polygon points="160,84 172,90 160,96" fill="#D97706"/>
            <text x="100" y="82" font-family="DM Sans" font-size="10" fill="#D97706" font-weight="500">Push</text>
            <!-- Pull arrow -->
            <line x1="260" y1="90" x2="200" y2="90" stroke="#44403C" stroke-width="2.5"/>
            <polygon points="200,84 188,90 200,96" fill="#44403C"/>
            <text x="240" y="82" font-family="DM Sans" font-size="10" fill="#44403C" font-weight="500">Pull</text>
            <!-- Anxiety up -->
            <line x1="180" y1="70" x2="180" y2="42" stroke="#78716C" stroke-width="2"/>
            <polygon points="174,42 180,30 186,42" fill="#78716C"/>
            <text x="196" y="48" font-family="DM Sans" font-size="10" fill="#78716C">Anxiety</text>
            <!-- Inertia down -->
            <line x1="180" y1="110" x2="180" y2="138" stroke="#78716C" stroke-width="2"/>
            <polygon points="174,138 180,150 186,138" fill="#78716C"/>
            <text x="196" y="140" font-family="DM Sans" font-size="10" fill="#78716C">Inertia</text>
        </svg>''',
    },
    "waarom-jouw-klant-niet-kiest-voor-winst": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Loss aversion curve -->
            <line x1="60" y1="90" x2="300" y2="90" stroke="#D6D3D1" stroke-width="1"/>
            <line x1="180" y1="20" x2="180" y2="160" stroke="#D6D3D1" stroke-width="1"/>
            <!-- Loss curve - steep, amber -->
            <path d="M 180 90 Q 140 90 100 155" stroke="#D97706" stroke-width="2.5" fill="none"/>
            <!-- Gain curve - shallow, grey -->
            <path d="M 180 90 Q 220 90 280 50" stroke="#A8A29E" stroke-width="2" fill="none"/>
            <!-- Reference dot -->
            <circle cx="180" cy="90" r="4" fill="#44403C"/>
            <!-- Labels -->
            <text x="80" y="170" font-family="DM Sans" font-size="12" fill="#D97706" font-weight="600">Verlies</text>
            <text x="260" y="42" font-family="DM Sans" font-size="12" fill="#A8A29E" font-weight="500">Winst</text>
            <!-- 2x annotation -->
            <text x="108" y="130" font-family="DM Sans" font-size="10" fill="#D97706">2×</text>
        </svg>''',
    },
    "impact-investor-shift-invest": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Investment filter funnel -->
            <text x="30" y="30" font-family="Instrument Serif" font-size="28" fill="#D6D3D1">"</text>
            <!-- Checklist -->
            <rect x="80" y="48" width="200" height="1" fill="#E7E5E4"/>
            <circle cx="90" cy="66" r="6" stroke="#D97706" stroke-width="1.5" fill="none"/>
            <path d="M 87 66 L 89 68 L 93 63" stroke="#D97706" stroke-width="1.5"/>
            <text x="104" y="70" font-family="DM Sans" font-size="11" fill="#44403C">Probleem groot genoeg?</text>
            <circle cx="90" cy="92" r="6" stroke="#D97706" stroke-width="1.5" fill="none"/>
            <path d="M 87 92 L 89 94 L 93 89" stroke="#D97706" stroke-width="1.5"/>
            <text x="104" y="96" font-family="DM Sans" font-size="11" fill="#44403C">Timing juist?</text>
            <circle cx="90" cy="118" r="6" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="104" y="122" font-family="DM Sans" font-size="11" fill="#44403C">Verdienmodel klopt?</text>
            <circle cx="90" cy="144" r="6" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="104" y="148" font-family="DM Sans" font-size="11" fill="#44403C">Team stuurt bij?</text>
        </svg>''',
    },
    "groei-zonder-groeipijn": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Step growth with gates -->
            <line x1="40" y1="155" x2="320" y2="155" stroke="#E7E5E4" stroke-width="1"/>
            <!-- Phase 1: flat -->
            <path d="M 50 140 L 110 140" stroke="#44403C" stroke-width="2.5"/>
            <!-- Gate 1 -->
            <line x1="120" y1="130" x2="120" y2="150" stroke="#D97706" stroke-width="2" stroke-dasharray="4 3"/>
            <!-- Phase 2: step up then flat -->
            <path d="M 130 105 L 200 105" stroke="#44403C" stroke-width="2.5"/>
            <line x1="120" y1="140" x2="130" y2="105" stroke="#44403C" stroke-width="2.5"/>
            <!-- Gate 2 -->
            <line x1="210" y1="95" x2="210" y2="115" stroke="#D97706" stroke-width="2" stroke-dasharray="4 3"/>
            <!-- Phase 3: step up then curve -->
            <path d="M 220 65 Q 270 60 310 40" stroke="#44403C" stroke-width="2.5"/>
            <line x1="210" y1="105" x2="220" y2="65" stroke="#44403C" stroke-width="2.5"/>
            <!-- Labels -->
            <text x="65" y="170" font-family="DM Sans" font-size="9" fill="#78716C">10 klanten</text>
            <text x="150" y="170" font-family="DM Sans" font-size="9" fill="#78716C">100</text>
            <text x="250" y="170" font-family="DM Sans" font-size="9" fill="#78716C">1.000</text>
            <!-- Gate labels -->
            <text x="110" y="125" font-family="DM Sans" font-size="8" fill="#D97706">gate</text>
            <text x="200" y="90" font-family="DM Sans" font-size="8" fill="#D97706">gate</text>
        </svg>''',
    },
    "fake-door-testing": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Fake door concept -->
            <!-- Door frame -->
            <rect x="130" y="30" width="100" height="120" rx="2" stroke="#44403C" stroke-width="2" fill="none"/>
            <!-- Door handle -->
            <circle cx="215" cy="90" r="4" stroke="#D97706" stroke-width="2" fill="none"/>
            <!-- CTA button inside door -->
            <rect x="150" y="75" width="60" height="22" rx="3" fill="#D97706" opacity="0.15"/>
            <text x="180" y="90" text-anchor="middle" font-family="DM Sans" font-size="9" fill="#D97706" font-weight="600">Bestel →</text>
            <!-- Measurement arrows -->
            <text x="155" y="55" font-family="DM Sans" font-size="9" fill="#78716C">Klikt?</text>
            <!-- Conversion indicator -->
            <text x="255" y="70" font-family="DM Sans" font-size="10" fill="#44403C">Conversie</text>
            <text x="255" y="88" font-family="DM Sans" font-size="20" fill="#D97706" font-weight="600">4,2%</text>
            <text x="255" y="105" font-family="DM Sans" font-size="10" fill="#78716C">→ doorgaan</text>
        </svg>''',
    },
    "bamboi-zebra-show": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Pivot arrow -->
            <text x="30" y="30" font-family="Instrument Serif" font-size="28" fill="#D6D3D1">"</text>
            <!-- B2C path (fading) -->
            <line x1="60" y1="110" x2="160" y2="110" stroke="#D6D3D1" stroke-width="2"/>
            <text x="60" y="100" font-family="DM Sans" font-size="10" fill="#A8A29E">B2C</text>
            <!-- X mark -->
            <line x1="155" y1="105" x2="165" y2="115" stroke="#A8A29E" stroke-width="2"/>
            <line x1="165" y1="105" x2="155" y2="115" stroke="#A8A29E" stroke-width="2"/>
            <!-- Pivot curve -->
            <path d="M 160 110 Q 200 110 220 75" stroke="#D97706" stroke-width="2.5" fill="none"/>
            <polygon points="216,68 224,68 220,58" fill="#D97706"/>
            <!-- B2B path (strong) -->
            <line x1="220" y1="70" x2="310" y2="70" stroke="#44403C" stroke-width="2.5"/>
            <polygon points="310,64 322,70 310,76" fill="#44403C"/>
            <text x="250" y="60" font-family="DM Sans" font-size="10" fill="#44403C" font-weight="600">B2B</text>
            <!-- Impact note -->
            <text x="250" y="140" font-family="DM Sans" font-size="10" fill="#78716C">Impact × volume</text>
        </svg>''',
    },
    "behavioral-design-principes": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- 7 principle icons in a row -->
            <!-- Principle circles -->
            <circle cx="60" cy="70" r="18" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="60" y="74" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#44403C" font-weight="600">1</text>
            <circle cx="105" cy="70" r="18" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="105" y="74" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#44403C" font-weight="600">2</text>
            <circle cx="150" cy="70" r="18" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="150" y="74" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#44403C" font-weight="600">3</text>
            <circle cx="195" cy="70" r="18" stroke="#D97706" stroke-width="2" fill="none"/>
            <text x="195" y="74" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#D97706" font-weight="600">4</text>
            <circle cx="240" cy="70" r="18" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="240" y="74" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#44403C" font-weight="600">5</text>
            <circle cx="285" cy="70" r="18" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="285" y="74" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#44403C" font-weight="600">6</text>
            <circle cx="330" cy="70" r="18" stroke="#44403C" stroke-width="1.5" fill="none"/>
            <text x="330" y="74" text-anchor="middle" font-family="DM Sans" font-size="12" fill="#44403C" font-weight="600">7</text>
            <!-- Subtitle -->
            <text x="60" y="120" font-family="DM Sans" font-size="11" fill="#78716C">Functionaliteit → Gedragsontwerp</text>
            <text x="60" y="140" font-family="DM Sans" font-size="10" fill="#A8A29E">Toetsen vóór lancering</text>
        </svg>''',
    },
    "kies-en-ontwerp-je-experiment": {
        "card": '''<svg viewBox="0 0 360 180" fill="none" xmlns="http://www.w3.org/2000/svg">
            <!-- Experiment selection matrix -->
            <!-- Aanname column -->
            <text x="40" y="35" font-family="DM Sans" font-size="10" fill="#78716C" font-weight="500">AANNAME</text>
            <text x="200" y="35" font-family="DM Sans" font-size="10" fill="#78716C" font-weight="500">EXPERIMENT</text>
            <line x1="40" y1="42" x2="320" y2="42" stroke="#E7E5E4" stroke-width="1"/>
            <!-- Row 1 -->
            <text x="40" y="66" font-family="DM Sans" font-size="11" fill="#44403C">Wenselijkheid</text>
            <text x="200" y="66" font-family="DM Sans" font-size="11" fill="#D97706">Fake door test</text>
            <line x1="175" y1="54" x2="195" y2="66" stroke="#D6D3D1" stroke-width="1"/>
            <!-- Row 2 -->
            <text x="40" y="96" font-family="DM Sans" font-size="11" fill="#44403C">Koopintentie</text>
            <text x="200" y="96" font-family="DM Sans" font-size="11" fill="#D97706">Concierge-test</text>
            <line x1="175" y1="84" x2="195" y2="96" stroke="#D6D3D1" stroke-width="1"/>
            <!-- Row 3 -->
            <text x="40" y="126" font-family="DM Sans" font-size="11" fill="#44403C">Haalbaarheid</text>
            <text x="200" y="126" font-family="DM Sans" font-size="11" fill="#D97706">Wizard-of-oz</text>
            <line x1="175" y1="114" x2="195" y2="126" stroke="#D6D3D1" stroke-width="1"/>
            <!-- Decision arrow -->
            <line x1="160" y1="150" x2="310" y2="150" stroke="#44403C" stroke-width="1.5"/>
            <polygon points="310,146 320,150 310,154" fill="#44403C"/>
            <text x="200" y="168" font-family="DM Sans" font-size="9" fill="#78716C">→ beslisbaar antwoord</text>
        </svg>''',
    },
}
