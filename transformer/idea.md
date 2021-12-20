# 1

卷积里的(h,w,c)->(h/4,w/4,d)通道数是由卷积核的个数决定的，那么这个通道数是我们自由确定的吗，它有什么意义呢？

超像素分割出来的块如果做外接最大矩，就保证不了数量上的一致

transunet输入要求：
CNN输入
固定尺寸，数量上的一致性

vit输入
数量上不一定

```python
class PosCNN(nn.Module):
    def __init__(self, in_chans, embed_dim=768, s=1):
        super(PosCNN, self).__init__()
        self.proj = nn.Sequential(nn.Conv2d(in_chans, embed_dim, 3, s, 1, bias=True, groups=embed_dim), )
        self.s = s

    def forward(self, x, H, W):
        B, N, C = x.shape
        feat_token = x
        cnn_feat = feat_token.transpose(1, 2).view(B, C, H, W)
        if self.s == 1:
            x = self.proj(cnn_feat) + cnn_feat
        else:
            x = self.proj(cnn_feat)
        x = x.flatten(2).transpose(1, 2)
        return x

    def no_weight_decay(self):
        return ['proj.%d.weight' % i for i in range(4)]
```

