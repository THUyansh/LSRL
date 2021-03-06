"""
验证集适配器
"""
from torch.utils.data import Dataset

from torchrec.data import IDataReader


class DevDataset(Dataset):
    """验证集适配器"""

    def __init__(self, data_reader: IDataReader):
        self.data_reader = data_reader

    def __len__(self):
        return self.data_reader.get_dev_dataset_size()

    def __getitem__(self, item):
        return self.data_reader.get_dev_dataset_item(item)
