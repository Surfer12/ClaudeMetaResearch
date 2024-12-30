from collections import defaultdict
from typing import Dict, List, Any
import numpy as np
from datetime import datetime, timedelta

class PatternMetrics:
    def __init__(self):
        self.pattern_counts = defaultdict(int)
        self.meta_levels = []
        self.script_counts = defaultdict(int)
        self.confidence_history = []
        self.timestamps = []
        
    def update_pattern_metrics(self, pattern: Any) -> None:
        """Update metrics with a new pattern observation."""
        self.pattern_counts[pattern.pattern_type] += 1
        self.meta_levels.append(pattern.meta_level)
        self.script_counts[pattern.script_type] += 1
        self.confidence_history.append(pattern.confidence)
        self.timestamps.append(datetime.now())
        
    def get_pattern_counts(self) -> Dict[str, int]:
        """Get the distribution of pattern types."""
        return dict(self.pattern_counts)
    
    def get_meta_level_progression(self) -> Dict[str, float]:
        """Analyze the progression of meta-cognitive levels."""
        if not self.meta_levels:
            return {"average": 0.0, "trend": 0.0}
            
        levels = np.array(self.meta_levels)
        trend = np.polyfit(range(len(levels)), levels, 1)[0]
        
        return {
            "average": float(np.mean(levels)),
            "trend": float(trend),
            "max": float(np.max(levels)),
            "min": float(np.min(levels))
        }
    
    def get_script_distribution(self) -> Dict[str, float]:
        """Get the distribution of script types."""
        total = sum(self.script_counts.values())
        if total == 0:
            return {}
            
        return {
            script: count / total
            for script, count in self.script_counts.items()
        }
    
    def get_confidence_trends(self) -> Dict[str, float]:
        """Analyze confidence score trends."""
        if not self.confidence_history:
            return {"average": 0.0, "trend": 0.0}
            
        confidence = np.array(self.confidence_history)
        trend = np.polyfit(range(len(confidence)), confidence, 1)[0]
        
        recent_window = 10
        recent_confidence = confidence[-recent_window:] if len(confidence) > recent_window else confidence
        
        return {
            "average": float(np.mean(confidence)),
            "trend": float(trend),
            "recent_average": float(np.mean(recent_confidence)),
            "volatility": float(np.std(confidence))
        }
    
    def get_time_based_metrics(self, window: timedelta = timedelta(hours=1)) -> Dict[str, Any]:
        """Get metrics within a specific time window."""
        if not self.timestamps:
            return {}
            
        now = datetime.now()
        window_start = now - window
        
        # Filter metrics within window
        recent_indices = [
            i for i, ts in enumerate(self.timestamps)
            if ts >= window_start
        ]
        
        if not recent_indices:
            return {}
            
        recent_confidence = [self.confidence_history[i] for i in recent_indices]
        recent_meta_levels = [self.meta_levels[i] for i in recent_indices]
        
        return {
            "window_size": str(window),
            "pattern_count": len(recent_indices),
            "average_confidence": float(np.mean(recent_confidence)),
            "average_meta_level": float(np.mean(recent_meta_levels)),
            "pattern_frequency": len(recent_indices) / window.total_seconds()
        } 