import pandas as pd

# Expanded industry skills dataset
industry_skills_data = {
    "skills": [
        "Python", "Data Science", "Machine Learning", "Deep Learning", "Tableau",
        "SQL", "Big Data", "Cloud Computing", "Cybersecurity", "Web Development",
        "Java", "JavaScript", "C++", "React", "Django", "Blockchain", "DevOps",
        "Product Management", "UI/UX Design", "Digital Marketing", "SEO", "Project Management"
    ],
    "courses": [
        ["Python for Beginners", "Advanced Python", "Python for Automation"],
        ["Intro to Data Science", "Data Science Bootcamp", "Statistics for Data Science"],
        ["Machine Learning A-Z", "Practical ML", "ML with Python & R"],
        ["Deep Learning Specialization", "Neural Networks", "AI & Deep Learning"],
        ["Tableau for Data Visualization", "Advanced Tableau", "Tableau Masterclass"],
        ["SQL for Beginners", "Advanced SQL Queries", "Database Management"],
        ["Big Data with Hadoop", "Spark for Big Data", "Data Engineering"],
        ["AWS Cloud Practitioner", "Azure Fundamentals", "Google Cloud Platform"],
        ["Cybersecurity Basics", "Ethical Hacking", "Network Security"],
        ["Full-Stack Web Development", "Frontend Development with React", "Backend with Node.js"],
        ["Java for Beginners", "Spring Boot Masterclass", "Java Advanced Concepts"],
        ["JavaScript Basics", "JavaScript ES6+", "Advanced JavaScript"],
        ["C++ Fundamentals", "Competitive Programming with C++", "Data Structures in C++"],
        ["React Crash Course", "React Native for Mobile Apps", "Next.js for Web Development"],
        ["Django for Web Apps", "Django REST Framework", "Full-Stack Django"],
        ["Blockchain Fundamentals", "Ethereum & Smart Contracts", "NFT Development"],
        ["DevOps with Docker", "Kubernetes for Beginners", "CI/CD Pipelines"],
        ["Product Management 101", "Agile & Scrum for Product Managers", "Roadmap Strategy"],
        ["UI/UX Design with Figma", "Wireframing & Prototyping", "User Research"],
        ["Digital Marketing Masterclass", "Social Media Marketing", "Paid Advertising"],
        ["SEO Optimization Strategies", "Keyword Research", "SEO & Content Marketing"],
        ["Project Management Fundamentals", "PMP Certification Prep", "Agile Project Management"]
    ]
}

# Convert to DataFrame
industry_skills_df = pd.DataFrame(industry_skills_data)

def analyze_skill_gap(current_skills):
    """Returns recommended courses for missing industry skills"""
    missing_skills = industry_skills_df[~industry_skills_df["skills"].isin(current_skills)]
    recommendations = {row["skills"]: row["courses"] for _, row in missing_skills.iterrows()}
    return recommendations
