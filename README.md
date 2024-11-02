# A flexible CTGAN that can be customized by conditioning on user-specified variables(s)

## 0.0 Introduction  
This repo modified the CTGAN official source code and made CTGAN conditional on any user-specified discrete columns for some research purposes.  

## 1.0 Usage

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

