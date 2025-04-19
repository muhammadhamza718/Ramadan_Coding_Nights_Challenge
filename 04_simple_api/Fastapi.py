"""
FastAPI Money Motivation API
===========================

A RESTful API service that provides random side hustle ideas and money-related quotes.
This API is designed to inspire and motivate users in their financial journey.

Features:
- Random side hustle suggestions
- Inspirational money quotes
- RESTful endpoints
- FastAPI framework implementation

Security Considerations:
- Input validation
- Rate limiting (to be implemented)
- CORS policies (to be implemented)
- API key authentication (to be implemented)

Author: [Your Name]
Version: 1.0.0
License: MIT
"""

from fastapi import FastAPI, HTTPException, Security
from fastapi.security import APIKeyHeader
from typing import Dict, List, Optional
import random
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app with metadata
app = FastAPI(
    title="Money Motivation API",
    description="An API for financial inspiration and side hustle ideas",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Data store - In a production environment, this would be in a database
side_hustles: List[str] = [
    "Freelancing - Start offering your skills online!",
    "Dropshipping - Sell without handling inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting products!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Sell custom-designed products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "YouTube Channel - Monetize videos through ads and sponsorships!",
    "Social Media Management - Manage accounts for brands and influencers!",
    "App Development - Create mobile or web applications for businesses!",
]

money_quotes: List[str] = [
    "The way to get started is to quit talking and begin doing. – Walt Disney",
    "Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "If you don't find a way to make money while you sleep, you will work until you die. – Warren Buffett",
    "Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "Money is a terrible master but an excellent servant. – P.T. Barnum",
    "You must gain control over your money or the lack of it will forever control you. – Dave Ramsey",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Don't stay in bed unless you can make money in bed. – George Burns",
    "Money often costs too much. – Ralph Waldo Emerson",
    "Never depend on a single income. Make an investment to create a second source. – Warren Buffett",
    "It's not about having lots of money. It's about knowing how to manage it. – Anonymous",
    "Rich people have small TVs and big libraries, and poor people have small libraries and big TVs. – Zig Ziglar",
    "Being rich is having money; being wealthy is having time. – Margaret Bonnano",
    "A wise person should have money in their head, but not in their heart. – Jonathan Swift",
    "Money grows on the tree of persistence. – Japanese Proverb",
]

# API Key security (to be implemented)
api_key_header = APIKeyHeader(name="X-API-Key")

@app.get("/", 
    response_model=Dict[str, str],
    summary="Root endpoint",
    description="Returns a welcome message and instructions for using the API"
)
async def read_root() -> Dict[str, str]:
    """
    Root endpoint that provides API information and available routes.
    
    Returns:
        Dict[str, str]: Welcome message and instructions
    """
    logger.info("Root endpoint accessed")
    return {
        "message": "Hello World, Go to /side_hustles or /money_quotes to get a random side hustle or money quote",
        "version": "1.0.0",
        "documentation": "/docs"
    }

@app.get("/side_hustles",
    response_model=Dict[str, str],
    summary="Get random side hustle",
    description="Returns a random side hustle idea from the collection"
)
async def get_side_hustles() -> Dict[str, str]:
    """
    Returns a random side hustle idea.
    
    Returns:
        Dict[str, str]: Random side hustle suggestion
        
    Raises:
        HTTPException: If the service is unavailable
    """
    try:
        logger.info("Side hustle requested")
        return {"side_hustle": random.choice(side_hustles)}
    except Exception as e:
        logger.error(f"Error getting side hustle: {str(e)}")
        raise HTTPException(status_code=500, detail="Service temporarily unavailable")

@app.get("/money_quotes",
    response_model=Dict[str, str],
    summary="Get random money quote",
    description="Returns a random inspirational quote about money"
)
async def get_money_quotes() -> Dict[str, str]:
    """
    Returns a random money-related quote.
    
    Returns:
        Dict[str, str]: Random money quote
        
    Raises:
        HTTPException: If the service is unavailable
    """
    try:
        logger.info("Money quote requested")
        return {"money_quote": random.choice(money_quotes)}
    except Exception as e:
        logger.error(f"Error getting money quote: {str(e)}")
        raise HTTPException(status_code=500, detail="Service temporarily unavailable")

# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Initialize services and resources on startup.
    """
    logger.info("API starting up...")
    # Add initialization code here (database connections, cache setup, etc.)

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Cleanup resources on shutdown.
    """
    logger.info("API shutting down...")
    # Add cleanup code here

# Health check endpoint
@app.get("/health",
    response_model=Dict[str, str],
    summary="Health check",
    description="Returns the health status of the API"
)
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint for monitoring.
    
    Returns:
        Dict[str, str]: Health status and timestamp
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }