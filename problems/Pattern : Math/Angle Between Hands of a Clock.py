class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        def to_min(hour,minutes):
            return hour*60+ minutes
        def get_hour_hand_angle(hour, minutes):
            return (0.5*to_min(hour,minutes))%360
        def get_min_hand_angle(minutes):
            return (6*minutes)%360
        hha=get_hour_hand_angle(hour,minutes)
        mha=get_min_hand_angle(minutes)
        return min(abs(hha-mha),360-abs(hha-mha))