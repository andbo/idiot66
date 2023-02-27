# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/routers/00_aroute.ipynb.

# %% auto 0
__all__ = ['router', 'aroute', 'second']

# %% ../../nbs/routers/00_aroute.ipynb 3
from fastapi import APIRouter

# %% ../../nbs/routers/00_aroute.ipynb 5
router = APIRouter()

# %% ../../nbs/routers/00_aroute.ipynb 6
@router.get('/aroute')
async def aroute():
    return {"message": "Welcome in aroute!"}

# %% ../../nbs/routers/00_aroute.ipynb 7
@router.get('/second')
async def second():
    return {"message": "Welcome in the second route!"}
