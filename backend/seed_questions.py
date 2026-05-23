from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.db.models import InterviewQuestion

questions = [
    {
        "skill": "Angular",
        "difficulty": "easy",
        "question": "What is Angular and why is it used?",
        "expected_topics": [
            "SPA",
            "TypeScript",
            "Component-based architecture",
            "Framework",
        ],
        "type": "curated",
        "tags": ["angular-core", "basics"],
    },
    {
        "skill": "Angular",
        "difficulty": "easy",
        "question": "Explain Angular components.",
        "expected_topics": [
            "Reusable UI",
            "Decorator",
            "Template",
            "Component lifecycle",
        ],
        "type": "curated",
        "tags": ["components", "architecture"],
    },
    {
        "skill": "Angular",
        "difficulty": "easy",
        "question": "What are Angular directives?",
        "expected_topics": [
            "Structural directives",
            "Attribute directives",
            "*ngIf",
            "*ngFor",
        ],
        "type": "curated",
        "tags": ["directives"],
    },
    {
        "skill": "Angular",
        "difficulty": "easy",
        "question": "What is data binding in Angular?",
        "expected_topics": [
            "Interpolation",
            "Property binding",
            "Event binding",
            "Two-way binding",
        ],
        "type": "curated",
        "tags": ["binding"],
    },
    {
        "skill": "Angular",
        "difficulty": "easy",
        "question": "Explain dependency injection in Angular.",
        "expected_topics": [
            "Injectable",
            "Service injection",
            "Provider",
            "Singleton services",
        ],
        "type": "curated",
        "tags": ["dependency-injection"],
    },
    {
        "skill": "Angular",
        "difficulty": "medium",
        "question": "Explain Angular lifecycle hooks.",
        "expected_topics": ["ngOnInit", "ngOnChanges", "ngOnDestroy", "Lifecycle flow"],
        "type": "curated",
        "tags": ["lifecycle-hooks"],
    },
    {
        "skill": "Angular",
        "difficulty": "medium",
        "question": "What is lazy loading in Angular?",
        "expected_topics": [
            "Feature modules",
            "Performance optimization",
            "Route-based loading",
        ],
        "type": "curated",
        "tags": ["lazy-loading", "performance"],
    },
    {
        "skill": "Angular",
        "difficulty": "medium",
        "question": "Explain Angular route guards.",
        "expected_topics": [
            "CanActivate",
            "Authentication",
            "Authorization",
            "Navigation control",
        ],
        "type": "curated",
        "tags": ["routing", "guards"],
    },
    {
        "skill": "Angular",
        "difficulty": "medium",
        "question": "What are Angular reactive forms?",
        "expected_topics": [
            "FormGroup",
            "FormControl",
            "Validation",
            "Reactive approach",
        ],
        "type": "curated",
        "tags": ["forms", "reactive-forms"],
    },
    {
        "skill": "Angular",
        "difficulty": "medium",
        "question": "Explain RxJS observables in Angular.",
        "expected_topics": [
            "Streams",
            "Subscriptions",
            "Async handling",
            "Reactive programming",
        ],
        "type": "curated",
        "tags": ["rxjs", "observables"],
    },
    {
        "skill": "Angular",
        "difficulty": "medium",
        "question": "What are Angular HTTP interceptors?",
        "expected_topics": [
            "Request interception",
            "Response handling",
            "Authentication tokens",
            "Global error handling",
        ],
        "type": "curated",
        "tags": ["http", "interceptors"],
    },
    {
        "skill": "Angular",
        "difficulty": "advanced",
        "question": "Explain Angular change detection strategy.",
        "expected_topics": [
            "Default strategy",
            "OnPush",
            "Zone.js",
            "Performance optimization",
        ],
        "type": "curated",
        "tags": ["change-detection", "performance"],
    },
    {
        "skill": "Angular",
        "difficulty": "advanced",
        "question": "How does Angular optimize performance in large applications?",
        "expected_topics": ["Lazy loading", "OnPush", "TrackBy", "Code splitting"],
        "type": "curated",
        "tags": ["performance", "optimization"],
    },
    {
        "skill": "Angular",
        "difficulty": "advanced",
        "question": "Explain state management approaches in Angular.",
        "expected_topics": ["NgRx", "RxJS", "Signals", "Global state"],
        "type": "curated",
        "tags": ["state-management"],
    },
    {
        "skill": "Angular",
        "difficulty": "advanced",
        "question": "What are Angular signals and how do they work?",
        "expected_topics": [
            "Reactive primitives",
            "Signal updates",
            "Computed",
            "Effects",
        ],
        "type": "curated",
        "tags": ["signals", "modern-angular"],
    },
    {
        "skill": "Angular",
        "difficulty": "advanced",
        "question": "How would you implement accessibility in Angular applications?",
        "expected_topics": [
            "ARIA",
            "Keyboard navigation",
            "Screen readers",
            "Semantic HTML",
        ],
        "type": "curated",
        "tags": ["accessibility", "wcag"],
    },
]


db: Session = SessionLocal()


for question in questions:

    db_question = InterviewQuestion(
        skill=question["skill"],
        difficulty=question["difficulty"],
        question=question["question"],
        expected_topics=question["expected_topics"],
        type=question["type"],
        tags=question["tags"],
    )

    db.add(db_question)


db.commit()

db.close()

print("Questions seeded successfully.")
