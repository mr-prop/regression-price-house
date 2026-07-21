from pydantic import BaseModel , Field


class HouseFeatures(BaseModel):
    """House information for prediction."""
    Square_Feet:float = Field(... , gt = 0,description="House area in square feet",example=150.5)
    Num_Bedrooms:int = Field(... , ge = 1,le = 5,description="Number of bedrooms",example=3)
    Num_Bathrooms:int = Field(... , ge = 1,le = 3,description="Number of bathrooms",example=2)
    Num_Floors:int = Field(... , ge = 1,le = 3,description="Number of floors",example=2)
    Year_Built:int = Field(... , ge = 1900,le = 2022,description="Construction year",example=2015)
    Has_Garden:int = Field(... , ge = 0,le = 1,description="0 = No, 1 = Yes",example=1)
    Has_Pool:int = Field(... , ge = 0,le = 1,description="0 = No, 1 = Yes",example=0)
    Garage_Size:int = Field(... , ge = 10,le = 49,description="Garage capacity",example=20)
    Location_Score:float = Field(... , ge = 0,le = 10,description="Location quality score",example=8.5)
    Distance_to_Center:float = Field(... , ge = 0,le = 20,description="Distance to city center (km)",example=5.2)