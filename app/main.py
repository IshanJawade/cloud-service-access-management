from fastapi import FastAPI
from app.routes import auth, permissions, plans, subscriptions, usage, cloud_services
from app.database import engine, Base


# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Initialize FastAPI app
app.include_router(plans.router)

app.include_router(subscriptions.router)

app.include_router(usage.router)

app.include_router(cloud_services.router)


app = FastAPI(title="Cloud Service Access Management System")

# Include route modules
app.include_router(auth.router)
app.include_router(permissions.router)
app.include_router(plans.router)
app.include_router(subscriptions.router)
app.include_router(usage.router)
app.include_router(cloud_services.router)
