import feetmeter

print(format("피트","10s"),"\t",format("미터","10s"),"\t","|  ",format("미터","10s"),"\t",format("피트","10s"),"\n",format("10.0", "10s"),
      "\t", format(feetmeter.feetToMeter(10), "6.3f"), "\t", "|  ", format("20.0", "10s"), "\t", format(feetmeter.meterToFeet(20), "6.3f"),"\n",
      format("2.0", "15s"),format(feetmeter.feetToMeter(2), "6.3f"), "\t", "|  ", format("25.0", "10s"), "\t", format(feetmeter.meterToFeet(25), "6.3f"),
      "\n...", "\n",format("9.0", "10s"),"\t", format(feetmeter.feetToMeter(9), "6.3f"), "\t", "|  ", format("60.0", "10s"), "\t", format(feetmeter.meterToFeet(60), "6.3f"),
      "\n", format("10.0", "10s"),"\t", format(feetmeter.feetToMeter(10), "6.3f"), "\t", "|  ", format("65.0", "10s"), "\t", format(feetmeter.meterToFeet(65), "6.3f"))
