# cli.py

import argparse
from materials import DesignCode

def parse_cli_args() -> dict:
    parser = argparse.ArgumentParser(description="RC Section Designer CLI")

    parser.add_argument('--code', type=lambda s:s.upper(), default='EUROCODE', choices=['EUROCODE', 'ACI'],
                        required=True, help='Design code to apply (default: EUROCODE)')
    parser.add_argument('--width_mm', type=float, required=True,
                        help='Section width in mm')
    parser.add_argument('--depth_mm', type=float, required=True,
                        help='Section depth in mm')
    parser.add_argument('--fck', type=float, required=True,
                        help='Characteristic concrete strength fck (MPa)')
    parser.add_argument('--fyk', type=float, required=True,
                        help='Characteristic steel strength fyk (MPa)')
    parser.add_argument("--save_diagram", action="store_true", help="Save plot as PNG")
    parser.add_argument(
        "--save_summary",
        action="store_true",
        help="Save material and geometry summary"
    )

    args = parser.parse_args()

    # FIX: Convert code string to Enum before return
    code_enum = DesignCode[args.code.upper()]

    return {
        'width_mm': args.width_mm,
        'depth_mm': args.depth_mm,
        'fck': args.fck,
        'fyk': args.fyk,
        'code': code_enum,
        'save_diagram': args.save_diagram,
        'save_summary': args.save_summary,
    }
