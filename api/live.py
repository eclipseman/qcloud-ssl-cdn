#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: 'eclipseman'
# time: 2025-3-13 17:42
import json

from datetime import datetime
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入 live 产品模块的 models
from tencentcloud.live.v20180801 import models

from api.get_client_profile import get_client_instance


def get_live_client_instance(id, key):
    '''获取live的实例，用于后面对live的各种操作
    '''
    client = get_client_instance(id, key, "live")
    return client


def get_live_detail_info(client):
    '''获取所有LIVE的详细信息，返回列表
    '''
    try:
        req = models.DescribeLiveDomainCertBindingsRequest()
        # 详细文档见 https://cloud.tencent.com/document/product/267/78656

        params = {}
        req.from_json_string(json.dumps(params))

        resp = client.DescribeLiveDomainCertBindings(req)
        print("获取所有live详细信息成功")
        return resp.LiveDomainCertBindings

    except TencentCloudSDKException as err:
        print(err)
        return []


def update_live_ssl(client, domain, cert_id):
    '''为指定域名的LIVE更换SSL证书
    '''
    try:
        req = models.ModifyLiveDomainCertBindingsRequest()
        # 详细文档见 https://cloud.tencent.com/document/product/267/78655

        params = {
            "CloudCertId": cert_id,
            "DomainInfos": [
                {
                    "DomainName": domain,
                    "Status": 1
                }
            ]
        }
        req.from_json_string(json.dumps(params))

        resp = client.ModifyLiveDomainCertBindings(req)
        print(resp.to_json_string())
        print("成功更新域名为{0}的LIVE的ssl证书为{1}".format(domain, cert_id))

    except TencentCloudSDKException as err:
        print(err)
        exit("为LIVE设置SSL证书{}出错".format(cert_id))
