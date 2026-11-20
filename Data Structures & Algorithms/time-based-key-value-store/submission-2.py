import bisect
class TimeMap:

    def __init__(self):
        self.key_hmaps = {}
        self.key_timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_hmaps:
            self.key_hmaps[key][timestamp] = value
            self.key_timestamps[key].append(timestamp)
        else:
            self.key_hmaps[key] = {timestamp: value}
            self.key_timestamps[key] = [timestamp]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_hmaps:
            return ""

        if timestamp in self.key_hmaps[key]:
            return self.key_hmaps[key][timestamp]
        
        
        if self.key_timestamps[key][0] > timestamp:
            return ""
        if self.key_timestamps[key][-1] <= timestamp:
            last_ts = self.key_timestamps[key][-1]
            return self.key_hmaps[key][last_ts]
        
        ts_index = bisect.bisect_left(self.key_timestamps[key], timestamp)
        closest_ts = self.key_timestamps[key][ts_index - 1]
        return self.key_hmaps[key][closest_ts]
                


        
