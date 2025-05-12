from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# 👇 This is the key line that tells FastAPI to enable security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# 👇 This function activates the security in OpenAPI
def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(status_code=401, detail="No token provided")
    return {"token": token}

@app.post("/token")
def login():
    # Just a dummy token endpoint
    return {"access_token": "exampletoken", "token_type": "bearer"}

@app.get("/secure-data")
def secure_data(user: dict = Depends(get_current_user)):
    return {"message": "You are authorized", "user": user}
