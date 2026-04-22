import numpy as np


class StepCounter:
    """
    One step counter class for both offline and real-time usage.
    You can add any other attributes you need to the class. But you should not change the interface of the class.
    """

    def __init__(self):
        """
        Initialize the step counter.
        """
        raise NotImplementedError

    def reset(self) -> None:
        """
        Reset internal state such as buffers and cumulative count.
        After reset(), total_steps should be 0.
        """
        raise NotImplementedError

    def update(self, data_chunk: dict) -> dict:
        """
        Real-time update: process a chunk of new samples.

        Input
          data_chunk["time"] : numpy.ndarray with shape (M,) [required]
          data_chunk["acc"]  : numpy.ndarray with shape (M, 3) in m/s^2 [required]
          data_chunk["gyro"] : numpy.ndarray with shape (M, 3) in rad/s [optional]
          data_chunk["mag"]  : numpy.ndarray with shape (M, 3) in uT [optional]
          Chunks arrive sequentially.

        Output (must contain all keys)
          {
            "new_steps": int,
            "total_steps": int,
            "new_step_timestamps": np.ndarray,  # shape (K,), float seconds
            "diagnostics": dict
          }
        """
        raise NotImplementedError

    def run_offline(self, data: dict) -> dict:
        """
        Offline processing: process a full recording.

        Input
          data["time"] : numpy.ndarray with shape (N,) [required]
          data["acc"]  : numpy.ndarray with shape (N, 3) in m/s^2 [required]
          data["gyro"] : numpy.ndarray with shape (N, 3) in rad/s [optional]
          data["mag"]  : numpy.ndarray with shape (N, 3) in uT [optional]

        Output format for grading (must contain all keys)
          {
            "step_count": int,
            "step_timestamps": np.ndarray,  # shape (K,), float seconds
            "diagnostics": dict
          }

        Requirements on output:
          - "step_count" must be a Python int and must be >= 0.
          - "step_timestamps" must be a 1D NumPy array of dtype float with shape (K,).
            Each entry is a timestamp in seconds. If your algorithm does not produce
            timestamps, return an empty array with shape (0,) rather than None.
          - "diagnostics" must be a Python dict. It may be empty.
        """
        raise NotImplementedError
