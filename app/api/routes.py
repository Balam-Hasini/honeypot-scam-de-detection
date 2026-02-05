from fastapi import APIRouter, Depends
from app.api.auth import verify_api_key
from app.core.scam_detector import detect_scam
from app.core.agent_orchestrator import run_agent
from app.intelligence.extractor import extract_intelligence
from app.database.session_store import store_message, get_history

router = APIRouter()

@router.post("/honeypot/message")
def honeypot(payload: dict, auth=Depends(verify_api_key)):
    session_id = payload["sessionId"]
    msg = payload["message"]["text"]

    store_message(session_id, "scammer", msg)
    history = get_history(session_id)

    scam = detect_scam(msg)

    if scam["is_scam"]:
        reply = run_agent(msg, history)
        extract_intelligence(session_id, msg)
    else:
        reply = "Okay, noted."

    store_message(session_id, "agent", reply)

    return {
        "status": "success",
        "reply": reply
    }
