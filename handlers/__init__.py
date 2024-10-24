from loader import dp  
from handlers import ref_program  

dp.include_router(ref_program.router)
