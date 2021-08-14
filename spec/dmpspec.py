# params under "required"

required = [
    {
        "name": "version",
        "pos": 0,
        "value": 0x0b
    },
    {
        "name": "system",
        "pos": 1,
        "value": 0x02
    },
    {
        "name": "instrument",
        "pos": 2,
        "value": 0x01
    },
]
# Position 3 - 6 are channel-wide parameters
# From here on, "value" represents the maximum expected byte value
operators = []
ym2612 = [
    {
        "name": "FM_DEPTH",
        "pos": 3,
        "range": 0x07
    },
    {
        "name": "OP1_FEEDBACK",
        "pos": 4,
        "range": 0x07
    },
    {
        "name": "ALGORITHM",
        "pos": 5,
        "range": 0x07
    },
    {
        "name": "AM_DEPTH",
        "pos": 6,
        "range": 0x07
    },
    operators
]

# Remaining positions are tied to operators 1-4,
# offset is based on the position of the first control in the first operator (7),
# with the op index (0-3) multiplied by the total number of controls (11)
for op in range(4):
    offset = 7 + (op * 11)
    operators.append(
        {
            "name": f"OP{op}_MULT", # Multiple
            "pos": offset+0,
            "range": 0x0f # 0-15
        },
        {
            "name": f"OP{op}_TL", # Total Level
            "pos": offset+1,
            "range": 0x7f # 0-127
        },
        {
            "name": f"OP{op}_AR", # Attack Rate
            "pos": offset+2,
            "range": 0x1f # 0-31
        },
        {
            "name": f"OP{op}_DR1", # Decay Rate
            "pos": offset+3,
            "range": 0x1f # 0-31
        },
        {
            "name": f"OP{op}_SL", # sustain Level
            "pos": offset+4,
            "range": 0x0f # 0-15
        },
        {
            "name": f"OP{op}_RR", # Release rate
            "pos": offset+5,
            "range": 0x0f # 0-15
        },
        {
            "name": f"OP{op}_AM", # Amp Mod Enable
            "pos": offset+6,
            "range": 0x01 # 0-1
        },
        {
            "name": f"OP{op}_RS", # Rate Scaling
            "pos": offset+7,
            "range": 0x01 # 0-1
        },
        {
            "name": f"OP{op}_DT", # Detune
            "pos": offset+8,
            "range": 0x07 # 0-7, spec says there's some bit shifting involved...
        },
        {
            "name": f"OP{op}_DR2", # Second Decay Rate
            "pos": offset+9,
            "range": 0x1f # I thought it was a 16 range valu, turns out its 32
        },
        {
            "name": f"OP{op}_SSGEG", # SSG-EG (whatever that stands for)
            "pos": offset+10,
            "range": 0x1f # I thought it was a 16 range valu, turns out its 32
        },

    )
