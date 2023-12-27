
from middlewares.subcsription import CheckSub
from loader import dp



if __name__ == "middlewares":
    dp.middleware.setup(CheckSub())
