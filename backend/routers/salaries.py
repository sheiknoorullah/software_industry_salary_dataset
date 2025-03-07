from fastapi import APIRouter, HTTPException, Query
from services.salary_service import get_high_paying_companies

router = APIRouter()


@router.get("/high-paying-companies")
async def high_paying_companies(limit: int = Query(10, description="limit the number of results")):
    """
    Endpoint to get the most high-paying companies.
    """
    try:
        companies = get_high_paying_companies(limit)
        return companies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
