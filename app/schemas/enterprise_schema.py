from pydantic import BaseModel, Field, ConfigDict

class EnterpriseBase(BaseModel):
    name: str = Field(..., description="Company name")
    year_of_foundation: int = Field(..., ge=1800, le=2100, description="Year the company was founded")
    cnpj: str = Field(..., min_length=14, max_length=18, description="Company CNPJ")
    telephone: str = Field(..., min_length=10, max_length=15, description="Contact phone number")
    social_value: float = Field(..., gt=0, description="Company's social capital")

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Tech Solutions",
                "year_of_foundation": 2005,
                "cnpj": "12.345.678/0001-99",
                "telephone": "(11) 98765-4321",
                "social_value": 500000.00
            }
        }
    )

class EnterpriseCreate(EnterpriseBase):
    pass

class EnterpriseOut(EnterpriseBase):
    id: int
    
    model_config = ConfigDict(from_attributes=True)
