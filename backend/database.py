import sqlite3

# Connect database
conn = sqlite3.connect(
    "resume_analyzer.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS resume_analysis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    filename TEXT,

    ats_score REAL,

    skills TEXT,

    recommended_roles TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

def save_analysis(
    filename,
    ats_score,
    skills,
    recommended_roles
):

    cursor.execute("""
    INSERT INTO resume_analysis (

        filename,
        ats_score,
        skills,
        recommended_roles

    )

    VALUES (?, ?, ?, ?)
    """, (

        filename,
        ats_score,
        ", ".join(skills),
        ", ".join(recommended_roles)

    ))

    conn.commit()

def get_all_analyses():

    cursor.execute("""
    SELECT * FROM resume_analysis
    ORDER BY created_at DESC
    """)

    return cursor.fetchall()