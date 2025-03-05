import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates

# Download data
morecurr_24 = yf.download(['EURUSD=X', 'GBPUSD=X', 'AUDUSD=X', 'CADUSD=X', 'NZDUSD=X'], 
                          start='2024-08-01', end='2025-01-31', interval='1d')

# Extract 'Close' prices and prepare time data
dates = morecurr_24.index
eurusd_data = morecurr_24['Close']['EURUSD=X']
gbpusd_data = morecurr_24['Close']['GBPUSD=X']
audusd_data = morecurr_24['Close']['AUDUSD=X']
cadusd_data = morecurr_24['Close']['CADUSD=X']
nzdusd_data = morecurr_24['Close']['NZDUSD=X']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot currencies unpack (as empty lists to begin animation)
a, = ax.plot([], [], label='Euro', color='blue')
b, = ax.plot([], [], label='British Pound', color='red')
c, = ax.plot([], [], label='Australian Dollar', color='yellow')
d, = ax.plot([], [], label='Canadian Dollar', color='green')
e, = ax.plot([], [], label='New Zealand Dollar', color='orange')

# Style
ax.set_title('Global currencies against the American Dollar in the last 6 months', fontsize = 16)
ax.set_xlabel('Date')
ax.set_ylabel('Exchange Value')
ax.grid(color='grey', linestyle='--', linewidth=0.5)
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Format 
# Set the x and y axis limits to prevent the plot from being blank
ax.set_xlim(dates[0], dates[-1])
ax.set_ylim(min([eurusd_data.min(), gbpusd_data.min(), audusd_data.min(), cadusd_data.min(), nzdusd_data.min()]),
            max([eurusd_data.max(), gbpusd_data.max(), audusd_data.max(), cadusd_data.max(), nzdusd_data.max()]))

# Format x-axis to show only months (major ticks at start of month)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y')) 
ax.xaxis.set_major_locator(mdates.MonthLocator())  
plt.xticks(rotation=45) 

# Animation update function
def update(frame):
    a.set_xdata(dates[:frame])
    a.set_ydata(eurusd_data[:frame])
    b.set_xdata(dates[:frame])
    b.set_ydata(gbpusd_data[:frame])
    c.set_xdata(dates[:frame])
    c.set_ydata(audusd_data[:frame])
    d.set_xdata(dates[:frame])
    d.set_ydata(cadusd_data[:frame])
    e.set_xdata(dates[:frame])
    e.set_ydata(nzdusd_data[:frame])

    return a, b, c, d, e

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=len(dates), interval=5)  # Speed up by making it 10x faster

# Show the plot
plt.show()

# Save the animation as an HTML file
ani.save(r'C:\Users\heath\Desktop\HFA_projects\PDA\week_3\Currency.gif', writer="pillow")
