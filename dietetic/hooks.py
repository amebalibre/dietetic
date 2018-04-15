"""Script post migration."""

# Available functions on openupgradelib:
# https://github.com/OCA/openupgradelib/blob/master/openupgradelib/openupgrade.py#L129
from openupgradelib import openupgrade


def _load_data(populate_models, cr, module_name='dietetic'):
    """Populate models.

    This method populate a list of models:
    :param populate_models: Tuples with name of files into
        ./data/hooks/load_data directory
    :param cr: Cursor
    :module_name: Name of your module
    """
    for _file in populate_models:
        filename = 'data/hooks/load_data/{file}.csv'.format(
            file=_file
        )

        # populate the model
        openupgrade.load_data(
            cr=cr,
            module_name=module_name,
            filename=filename,
        )


def populate_post_init_hook(cr, registry):
    """Execute population of models."""
    # Tuples of files without extension. See ./data/hooks/load_data/*
    populate_models = (
        'category',
        'measure',
        'season',
    )
    _load_data(populate_models, cr)
