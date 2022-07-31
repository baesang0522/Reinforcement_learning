import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F


class Encoder(nn.Module):
    def __init__(self, num_input_channel, base_channel_size, latent_dim):
        super(Encoder, self).__init__()
        c_hid = base_channel_size

        self.encoder = nn.Sequential(
            nn.Conv2d(in_channels=num_input_channel,
                      out_channels=c_hid,
                      kernel_size=3,
                      stride=2,
                      padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=c_hid,
                      out_channels=c_hid,
                      kernel_size=3,
                      padding=1),
            nn.ReLU(),
            nn.Conv2d(in_channels=c_hid,
                      out_channels=2*c_hid,
                      kernel_size=3,
                      stride=2,
                      padding=1),
            nn.ReLU(),
            nn.Flatten(),
            nn.Linear(2*16*c_hid, latent_dim)
        )

    def forward(self, x):
        return self.encoder(x)


class Decoder(nn.Module):
    def __init__(self, num_input_channel, base_channel_size, latent_dim):
        super(Decoder, self).__init__()
        c_hid = base_channel_size
        self.linear = nn.Sequential(
            nn.Linear(latent_dim, 2 * 16 * c_hid),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(in_channels=2*c_hid,
                               out_channels=c_hid,
                               kernel_size=3,
                               output_padding=1,
                               padding=1,
                               stride=2),
            nn.ReLU(),
            nn.Conv2d(in_channels=c_hid,
                      out_channels=c_hid,
                      kernel_size=3,
                      padding=1),
            nn.ReLU(),
            nn.ConvTranspose2d(in_channels=c_hid,
                               out_channels=num_input_channel,
                               kernel_size=3,
                               output_padding=1,
                               padding=1,
                               stride=2),
            nn.Tanh()
        )

    def forward(self, x):
        x = self.linear(x)
        x = x.reshape(x.shape[0], -1, 4, 4)
        x = self.decoder(x)
        return x

