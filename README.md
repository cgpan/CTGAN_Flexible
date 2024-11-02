# A flexible CTGAN that can be customized by conditioning on user-specified variables(s)

## 0.0 Introduction  
This repo modified the [CTGAN official source code](https://github.com/sdv-dev/CTGAN) and made CTGAN conditional on any user-specified discrete columns for some research purposes.  

## 1.0 Usage  

The usage is similar to the original version of CTGAN; I added an extra parameter `user_specified_col=` in class objects like  `CTGAN` and `DataSampler.`   

To avoid future package conflicts, please uninstall the `ctgan` library from your environment if you already installed it.  
```{python}
pip uninstall ctgan
```

Download this repo to your project file path, then you can use it as the orginal `ctgan.` One example is:   
```{Python}
# import the modules
from ctgan import CTGAN
from ctgan import load_demo
from ctgan.data_sampler import DataSampler
from ctgan.data_transformer import DataTransformer
import seaborn as sns
import matplotlib.pyplot as plt

# load the data
real_data = load_demo()

# specifiy all discrete columns
discrete_columns = [
    'workclass',
    'education',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'native-country',
    'income'
]

# specificy the specific discrete column(s) you want to condition on
# this must be a list containing the strings of column names
controlled_col = ["sex", "race"]

# instantiate a CTGAN object
ctgan = CTGAN(epochs=50, cuda=True, verbose=True)

# fit ctgan model
ctgan.fit(real_data, discrete_columns, user_specified_col=controlled_col)

# plot the training loss
loss_df = ctgan.loss_values  # Retrieve the loss DataFrame

plt.figure(figsize=(10, 6))
plt.plot(loss_df['Epoch'], loss_df['Generator Loss'], label='Generator Loss', color='blue')
plt.plot(loss_df['Epoch'], loss_df['Discriminator Loss'], label='Discriminator Loss', color='orange')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('CTGAN Training Loss Over Epochs')
plt.legend()
plt.grid(True)
plt.show()

# generate synthetic data
synthetic_data = ctgan.sample(32561)
```

By default, the parameter `user_specified_col=None`. If you do not specify any columns, this function will run the same to the original `ctgan.`


## 2.0 SDV/CTGAN Official Resources

CTGAN is a collection of Deep Learning based synthetic data generators for single table data, which are able to learn from real data and generate synthetic data with high fidelity.

| Important Links                               |                                                                      |
| --------------------------------------------- | -------------------------------------------------------------------- |
| :computer: **[Website]**                      | Check out the SDV Website for more information about our overall synthetic data ecosystem.|
| :orange_book: **[Blog]**                      | A deeper look at open source, synthetic data creation and evaluation.|
| :book: **[Documentation]**                    | Quickstarts, User and Development Guides, and API Reference.         |
| :octocat: **[Repository]**                    | The link to the Github Repository of this library.                   |
| :keyboard: **[Development Status]**           | This software is in its Pre-Alpha stage.                             |
| [![][Slack Logo] **Community**][Community]    | Join our Slack Workspace for announcements and discussions.          |

[Website]: https://sdv.dev
[Blog]: https://datacebo.com/blog
[Documentation]: https://bit.ly/sdv-docs
[Repository]: https://github.com/sdv-dev/CTGAN
[License]: https://github.com/sdv-dev/CTGAN/blob/main/LICENSE
[Development Status]: https://pypi.org/search/?c=Development+Status+%3A%3A+2+-+Pre-Alpha
[Slack Logo]: https://github.com/sdv-dev/SDV/blob/stable/docs/images/slack.png
[Community]: https://bit.ly/sdv-slack-invite

Currently, this library implements the **CTGAN** and **TVAE** models described in the [Modeling Tabular data using Conditional GAN](https://arxiv.org/abs/1907.00503) paper, presented at the 2019 NeurIPS conference.

