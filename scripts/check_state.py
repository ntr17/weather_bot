"""Check current state before reset."""
from core.storage import load_state

s = load_state(5000)
print(f"balance={s['balance']}")
print(f"starting_balance={s.get('starting_balance', '?')}")
print(f"wins={s['wins']}")
print(f"losses={s['losses']}")
print(f"total_trades={s.get('total_trades', '?')}")
