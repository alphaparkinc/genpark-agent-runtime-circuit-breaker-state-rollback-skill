from client import AgentRuntimeCircuitBreakerStateRollbackClient

def main():
    client = AgentRuntimeCircuitBreakerStateRollbackClient()
    res = client.trigger_rollback("session_agent_finance_8819", 3)
    print(f"Status: {res['circuit_breaker_status']}")
    print(f"Restored Checkpoint: {res['restored_checkpoint_id']}")
    print(f"Integrity Verified: {res['state_integrity_verified']}")

if __name__ == "__main__":
    main()
