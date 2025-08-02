import React, { useState } from 'react';
import { Card, CardContent } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const sampleData = [
  { date: 'Week 1', score: 48, premium: 1200 },
  { date: 'Week 2', score: 45, premium: 1150 },
  { date: 'Week 3', score: 42, premium: 1100 },
  { date: 'Week 4', score: 38, premium: 1050 },
];

export default function Dashboard() {
  const [driverStats, setDriverStats] = useState({
    avg_speed: 55,
    harsh_braking: 3,
    rapid_accel: 2,
    night_driving_pct: 0.3,
    mileage_per_day: 35,
  });

  const [predictedScore, setPredictedScore] = useState(null);

  const fetchScore = async () => {
    // Replace with actual API call to Python backend
    const mockResponse = { score: 40 };
    setPredictedScore(mockResponse.score);
  };

  return (
    <div className="p-6 grid grid-cols-1 gap-6 max-w-3xl mx-auto">
      <Card>
        <CardContent className="space-y-4">
          <h2 className="text-xl font-semibold">Driving Behavior Summary</h2>
          <div className="grid grid-cols-2 gap-4">
            {Object.entries(driverStats).map(([key, value]) => (
              <div key={key} className="text-sm">
                <span className="font-medium">{key.replace(/_/g, ' ')}:</span> {value}
              </div>
            ))}
          </div>
          <Button onClick={fetchScore}>Get Risk Score</Button>
          {predictedScore !== null && (
            <div className="mt-2 text-lg font-semibold">
              Predicted Risk Score: {predictedScore}
            </div>
          )}
        </CardContent>
      </Card>

      <Card>
        <CardContent>
          <h2 className="text-xl font-semibold mb-4">Risk Score & Premium History</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={sampleData}>
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="score" stroke="#8884d8" name="Risk Score" />
              <Line type="monotone" dataKey="premium" stroke="#82ca9d" name="Premium ($)" />
            </LineChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
    </div>
  );
}
