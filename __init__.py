from .gcp_storage import NODE_CLASS_MAPPINGS as GCP_NODE_CLASS_MAPPINGS
from .gcp_storage import NODE_DISPLAY_NAME_MAPPINGS as GCP_NODE_DISPLAY_NAME_MAPPINGS

from .batch_tester import NODE_CLASS_MAPPINGS as BATCH_TESTER_NODE_CLASS_MAPPINGS
from .batch_tester import NODE_DISPLAY_NAME_MAPPINGS as BATCH_TESTER_NODE_DISPLAY_NAME_MAPPINGS

NODE_CLASS_MAPPINGS = {**GCP_NODE_CLASS_MAPPINGS, **BATCH_TESTER_NODE_CLASS_MAPPINGS}
NODE_DISPLAY_NAME_MAPPINGS = {**GCP_NODE_DISPLAY_NAME_MAPPINGS, **BATCH_TESTER_NODE_DISPLAY_NAME_MAPPINGS}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']