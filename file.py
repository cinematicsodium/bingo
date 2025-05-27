from random import choice

import pandas as pd
import streamlit as st

ONE = "dále'é"
TWO = "naaki"
THREE = "tai'"
FOUR = "dį́į́'"
FIVE = "ąąshdlai'"
SIX = "guustáni"
SEVEN = "guusts'iidi"
EIGHT = "tsąąbi'"
NINE = "ńguust'ai'"
TEN = "guneenani"

AFFIX_ONE = "łe"
SUFFIX_TEN = "dzáa'da"

TWENTY = "naadini"
THIRTY = "tàdini"
FORTY = f"{FOUR[:-1]}shdini"
FIFTY = f"{FIVE[:-2]}dini"
SIXTY = f"{SIX[:5]}ą́dini"
SEVENTY = f"{SEVEN}dini"

BINGO: dict[str, dict[int, str]] = {
    "B": {
        1: ONE,
        2: TWO,
        3: THREE,
        4: FOUR,
        5: FIVE,
        6: SIX,
        7: SEVEN,
        8: EIGHT,
        9: NINE,
        10: TEN,
        11: f"{AFFIX_ONE} {SUFFIX_TEN}",
        12: f"{TWO} {SUFFIX_TEN}",
        13: f"{THREE} {SUFFIX_TEN}",
        14: f"{FOUR} {SUFFIX_TEN}",
        15: f"{FIVE} {SUFFIX_TEN}",
    },
    "I": {
        16: f"{SIX} {SUFFIX_TEN}",
        17: f"{SEVEN} {SUFFIX_TEN}",
        18: f"{EIGHT} {SUFFIX_TEN}",
        19: f"{NINE} {SUFFIX_TEN}",
        20: TWENTY,
        21: f"{TWENTY} {AFFIX_ONE}",
        22: f"{TWENTY} {TWO}",
        23: f"{TWENTY} {THREE}",
        24: f"{TWENTY} {FOUR}",
        25: f"{TWENTY} {FIVE}",
        26: f"{TWENTY} {SIX}",
        27: f"{TWENTY} {SEVEN}",
        28: f"{TWENTY} {EIGHT}",
        29: f"{TWENTY} {NINE}",
        30: THIRTY,
    },
    "N": {
        31: f"{THIRTY} {AFFIX_ONE}",
        32: f"{THIRTY} {TWO}",
        33: f"{THIRTY} {THREE}",
        34: f"{THIRTY} {FOUR}",
        35: f"{THIRTY} {FIVE}",
        36: f"{THIRTY} {SIX}",
        37: f"{THIRTY} {SEVEN}",
        38: f"{THIRTY} {EIGHT}",
        39: f"{THIRTY} {NINE}",
        40: FORTY,
        41: f"{FORTY} {AFFIX_ONE}",
        42: f"{FORTY} {TWO}",
        43: f"{FORTY} {THREE}",
        44: f"{FORTY} {FOUR}",
        45: f"{FORTY} {FIVE}",
    },
    "G": {
        46: f"{FORTY} {SIX}",
        47: f"{FORTY} {SEVEN}",
        48: f"{FORTY} {EIGHT}",
        49: f"{FORTY} {NINE}",
        50: FIFTY,
        51: f"{FIFTY} {AFFIX_ONE}",
        52: f"{FIFTY} {TWO}",
        53: f"{FIFTY} {THREE}",
        54: f"{FIFTY} {FOUR}",
        55: f"{FIFTY} {FIVE}",
        56: f"{FIFTY} {SIX}",
        57: f"{FIFTY} {SEVEN}",
        58: f"{FIFTY} {EIGHT}",
        59: f"{FIFTY} {NINE}",
        60: SIXTY,
    },
    "O": {
        61: f"{SIXTY} {AFFIX_ONE}",
        62: f"{SIXTY} {TWO}",
        63: f"{SIXTY} {THREE}",
        64: f"{SIXTY} {FOUR}",
        65: f"{SIXTY} {FIVE}",
        66: f"{SIXTY} {SIX}",
        67: f"{SIXTY} {SEVEN}",
        68: f"{SIXTY} {EIGHT}",
        69: f"{SIXTY} {NINE}",
        70: SEVENTY,
        71: f"{SEVENTY} {AFFIX_ONE}",
        72: f"{SEVENTY} {TWO}",
        73: f"{SEVENTY} {THREE}",
        74: f"{SEVENTY} {FOUR}",
        75: f"{SEVENTY} {FIVE}",
    },
}


def draw_bingo_number() -> tuple[str, int, str] | None:
    """Draw a random bingo number from the BINGO card."""
    column = choice(list(BINGO.keys()))
    if not BINGO[column]:
        return None
    number = choice(list(BINGO[column].keys()))
    translation = BINGO[column].pop(number)
    bingo_items = column, number, translation
    return bingo_items


def main():

    st.title("Bingo Number Drawer")

    if "bingo_numbers" not in st.session_state:
        st.session_state.bingo_numbers = BINGO.copy()

    if "drawn_numbers" not in st.session_state:
        st.session_state.drawn_numbers = []

    if st.button("Draw a Bingo Number"):
        column = choice(list(st.session_state.bingo_numbers.keys()))
        if len(st.session_state.bingo_numbers[column]) == 0:
            st.write(f"No more numbers left in column {column}.")
            return

        number = choice(list(st.session_state.bingo_numbers[column].keys()))

        translation = st.session_state.bingo_numbers[column].pop(number)

        st.markdown(f"# {column}: {translation}")
        st.markdown(f"## {column}: {number}")

        st.session_state.drawn_numbers.append((column, number, translation))

        drawn_numbers: list[tuple[str, str]] = [
            (f"{column}: {number}", f"{column}: {translation}")
            for column, number, translation in st.session_state.drawn_numbers
        ]
        data = pd.DataFrame(drawn_numbers, columns=["Number", "Translation"])
        st.write("All Drawn Numbers:")
        st.write(data)
        st.write("Press the button to draw another Bingo number.")
    else:
        st.write("Press the button to draw a Bingo number.")


if __name__ == "__main__":
    main()
