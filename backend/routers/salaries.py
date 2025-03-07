from fastapi import APIRouter, HTTPException, Query
from services.salary_service import *

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


@router.get("/common-job-titles")
async def common_job_titles(limit: int = Query(10, description="limit the number of results")):
    """
    Endpoint to get the most common job titles.
    """
    try:
        job_titles = get_most_common_job_titles(limit)
        return job_titles
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/salary-trends-by-location")
async def salary_trends_by_location():
    """
    Endpoint to get salary trends by location.
    """
    try:
        trends = get_salary_trends_by_location()
        return trends
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/salary-by-company-rating")
async def salary_by_company_rating():
    """
    Endpoint to get the average salary for each company rating.
    """
    try:
        results = get_salary_by_company_rating()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/salary-distribution-by-job-title")
async def salary_distribution_by_job_title():
    """
    Endpoint to get the salary distribution by job title.
    """
    try:
        distribution = get_salary_distribution_by_job_title()
        return distribution
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/employment-status-and-salary")
async def employment_status_and_salary():
    """
    Endpoint to get the relationship between employment status and salary.
    """
    try:
        relationship = get_employment_status_and_salary()
        return relationship
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
