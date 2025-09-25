from fastapi import FastAPI, HTTPException
from database import init_db, get_db_connection
from models import User, Poll, Vote

app = FastAPI(title="PulseAI Backend")

# Initialize DB
init_db()

@app.post("/users/")
def create_user(user: User):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email))
        conn.commit()
        return {"message": "User created"}
    except:
        raise HTTPException(status_code=400, detail="User already exists")
    finally:
        conn.close()

@app.post("/polls/")
def create_poll(poll: Poll):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO polls (question, option_a, option_b) VALUES (?, ?, ?)",
                   (poll.question, poll.option_a, poll.option_b))
    conn.commit()
    conn.close()
    return {"message": "Poll created"}

@app.get("/polls/")
def get_polls():
    conn = get_db_connection()
    polls = conn.execute("SELECT * FROM polls").fetchall()
    conn.close()
    return [dict(p) for p in polls]

@app.post("/vote/")
def vote(vote: Vote):
    conn = get_db_connection()
    cursor = conn.cursor()
    if vote.option == "A":
        cursor.execute("UPDATE polls SET votes_a = votes_a + 1 WHERE id = ?", (vote.poll_id,))
    elif vote.option == "B":
        cursor.execute("UPDATE polls SET votes_b = votes_b + 1 WHERE id = ?", (vote.poll_id,))
    else:
        raise HTTPException(status_code=400, detail="Invalid option")
    conn.commit()
    conn.close()
    return {"message": "Vote recorded"}
