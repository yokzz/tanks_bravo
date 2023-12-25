from environs import Env
from dataclasses import dataclass

@dataclass
class Screen:
    height: int
    width: int
    
@dataclass
class Settings:
    screen: Screen
    
def get_settings(path: int): # 
    env = Env()
    env.read_env(path)
    
    return Settings(
        screen = Screen(
            height=env.int('HEIGHT'),
            width=env.int('WIDTH')
        )
    )
    
settings = get_settings('display_settings')
print(settings)