
from typing import List, Optional, Dict, Set
from pyterraformer.core.resources import ResourceObject
from pyterraformer.core.generics import BlockList, BlockSet
from pyterraformer.core.objects import ObjectMetadata
from dataclasses import dataclass



# this block can contain multiple items, items in a list are required
@dataclass 
class SnapshotEncryptionKeyItem():
        # non-optional-blocks
        raw_key: Optional[str] = None
        
# wrapper list class
class SnapshotEncryptionKey(BlockList):
        items: List[SnapshotEncryptionKeyItem]




# this block can contain multiple items, items in a list are required
@dataclass 
class SourceDiskEncryptionKeyItem():
        # non-optional-blocks
        raw_key: Optional[str] = None
        
# wrapper list class
class SourceDiskEncryptionKey(BlockList):
        items: List[SourceDiskEncryptionKeyItem]




# this block accepts only a single value, set the class directly
@dataclass 
class Timeouts():
        # non-optional-blocks
        create: Optional[str] = None
        delete: Optional[str] = None
        update: Optional[str] = None




class GoogleComputeSnapshot(ResourceObject):
    """    
    Args:
        name (str): 
        source_disk (str): 
    """
    _type = 'google_compute_snapshot'
    
    def __init__(self,
        tf_id: str,
        name:str,
        source_disk:str,
        # non-optional-blocks
        #optional
        metadata: Optional[ObjectMetadata] = None,
        description: Optional[str] = None,
        id: Optional[str] = None,
        labels: Optional[Dict[str, str]] = None,
        project: Optional[str] = None,
        snapshot_encryption_key_raw: Optional[str] = None,
        source_disk_encryption_key_raw: Optional[str] = None,
        zone: Optional[str] = None,
        snapshot_encryption_key: Optional[SnapshotEncryptionKey]=None,
        source_disk_encryption_key: Optional[SourceDiskEncryptionKey]=None,
        timeouts: Optional[Timeouts]=None,
        ):
            kwargs = {}
            if name is not None:
                kwargs['name'] = name
            if source_disk is not None:
                kwargs['source_disk'] = source_disk
            if description is not None:
                kwargs['description'] = description
            if id is not None:
                kwargs['id'] = id
            if labels is not None:
                kwargs['labels'] = labels
            if project is not None:
                kwargs['project'] = project
            if snapshot_encryption_key_raw is not None:
                kwargs['snapshot_encryption_key_raw'] = snapshot_encryption_key_raw
            if source_disk_encryption_key_raw is not None:
                kwargs['source_disk_encryption_key_raw'] = source_disk_encryption_key_raw
            if zone is not None:
                kwargs['zone'] = zone
            if snapshot_encryption_key is not None:
                kwargs['snapshot_encryption_key'] = snapshot_encryption_key
            if source_disk_encryption_key is not None:
                kwargs['source_disk_encryption_key'] = source_disk_encryption_key
            if timeouts is not None:
                kwargs['timeouts'] = timeouts
            
            super().__init__(tf_id=tf_id, metadata=metadata, **kwargs)
            
        
        