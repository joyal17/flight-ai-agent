import httpx

async def get_all_flights():
    url="https://opensky-network.org/api/states/all"

    async with httpx.AsyncClient(timeout=10.0) as client:
        try: 
            response= await client.get(url)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            print(f"HTTP error : {e}")

        except httpx.connectError as e:
            print(f"connection error :{e}")

        except httpx.TimeoutException as e:
            print(f"Request timed out :{e}")
    

    

    
async def get_flight_by_callsign(callsign:str):
    data =await get_all_flights()
    states=data["states"]
    for state in states:
        if state[1] and state[1].strip().upper() == callsign.upper():
            return {
            "icao24": state[0],
            "callsign": state[1].strip(),
            "country": state[2],
            "longitude": state[5],
            "latitude": state[6],
            "altitude": state[7],
            "on_ground": state[8],
            "speed_mps": state[9],
            "heading": state[10]
            }
    
    return None
