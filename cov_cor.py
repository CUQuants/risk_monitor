import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from data_manager import *

class CovCar():
    
    def __init__(self):
        
        data_manager = DataManager()
        self.market_returns = data_manager.market_returns
        self.fund_returns = data_manager.fund_return
        self.total_returns = pd.concat([self.market_returns, self.fund_returns], axis = 1)
        self.get_graphs()
        
    
    def get_graphs(self):
        
        self.make_plots(self.market_returns, "market returns")
        self.make_plots(self.fund_returns, "fund returns")
        self.make_plots(self.total_returns, "total returns")
    
    def make_plots(self, df, security_type):
        
        fig, axes = plt.subplots(1, 2, figsize = (30,10))
        
        df_corr = df.corr()
        df_cov = df.cov()
        
        sns.heatmap(df_corr, ax = axes[0])
        axes[0].set_title("Daily Adjusted Close {} Correlation Matrix from {} to {}".format(security_type,
                                                                                            df.index[0],
                                                                                            df.index[len(df) - 1]))
        
        sns.heatmap(df_cov, axes = axes[1])
        axes[1].set_title("Daily Adjusted Close {} Covariance Matrix from {} to {}".format(security_type,
                                                                                           df.index[0],
                                                                                           df.index[len(df) - 1]))
        current_directory = os.getcwd()
        graph_path = os.path.join(current_directory, "graphs")
        end_path = os.path.join(graph_path, "{}_matrices.png".format(security_type))
        plt.savefig(end_path)