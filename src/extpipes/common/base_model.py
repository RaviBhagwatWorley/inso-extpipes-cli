from pydantic_settings import BaseSettings, SettingsConfigDict


def to_hyphen_case(value: str) -> str:
    """Creates alias names from Python compatible snake_case '_' to yaml typical kebap-style ('-')
    # https://www.freecodecamp.org/news/snake-case-vs-camel-case-vs-pascal-case-vs-kebab-case-whats-the-difference/

    Args:
        value (str): the value to generate an alias for

    Returns:
        str: alias in hyphen-style
    """
    return value.replace("_", "-")


class Model(BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        # generate for each field an alias in hyphen-case (kebap)
        alias_generator=to_hyphen_case,
        # an aliased field may be populated by its name as given by the model attribute, as well as the alias
        # this supports both cases to be mixed
        populate_by_name=True
    )
