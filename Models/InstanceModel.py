from dataclasses import dataclass
from typing import Optional, List, Any
from datetime import datetime


@dataclass
class Ebs:
    attach_time: Optional[str] = None
    delete_on_termination: Optional[bool] = None
    status: Optional[str] = None
    volume_id: Optional[str] = None


@dataclass
class BlockDeviceMapping:
    device_name: Optional[str] = None
    ebs: Optional[Ebs] = None


@dataclass
class CapacityReservationSpecification:
    capacity_reservation_preference: Optional[str] = None


@dataclass
class CPUOptions:
    core_count: Optional[int] = None
    threads_per_core: Optional[int] = None


@dataclass
class EnclaveOptions:
    enabled: Optional[bool] = None


@dataclass
class HibernationOptions:
    configured: Optional[bool] = None


@dataclass
class MetadataOptions:
    state: Optional[str] = None
    http_tokens: Optional[str] = None
    http_put_response_hop_limit: Optional[int] = None
    http_endpoint: Optional[str] = None
    http_protocol_ipv6: Optional[str] = None


@dataclass
class Monitoring:
    state: Optional[str] = None


@dataclass
class Association:
    ip_owner_id: Optional[str] = None
    public_dns_name: Optional[str] = None
    public_ip: Optional[str] = None


@dataclass
class Attachment:
    attach_time: Optional[str] = None
    attachment_id: Optional[str] = None
    delete_on_termination: Optional[bool] = None
    device_index: Optional[int] = None
    status: Optional[str] = None
    network_card_index: Optional[int] = None


@dataclass
class Group:
    group_name: Optional[str] = None
    group_id: Optional[str] = None


@dataclass
class PrivateIPAddress:
    association: Optional[Association] = None
    primary: Optional[bool] = None
    private_dns_name: Optional[str] = None
    private_ip_address: Optional[str] = None


@dataclass
class NetworkInterface:
    association: Optional[Association] = None
    attachment: Optional[Attachment] = None
    description: Optional[str] = None
    groups: Optional[List[Group]] = None
    ipv6_addresses: Optional[List[Any]] = None
    mac_address: Optional[str] = None
    network_interface_id: Optional[str] = None
    owner_id: Optional[str] = None
    private_dns_name: Optional[str] = None
    private_ip_address: Optional[str] = None
    private_ip_addresses: Optional[List[PrivateIPAddress]] = None
    source_dest_check: Optional[bool] = None
    status: Optional[str] = None
    subnet_id: Optional[str] = None
    vpc_id: Optional[str] = None
    interface_type: Optional[str] = None


@dataclass
class Placement:
    availability_zone: Optional[str] = None
    group_name: Optional[str] = None
    tenancy: Optional[str] = None


@dataclass
class State:
    code: Optional[int] = None
    name: Optional[str] = None


@dataclass
class Tag:
    key: Optional[str] = None
    value: Optional[str] = None


@dataclass
class Instance:
    ami_launch_index: Optional[int] = None
    image_id: Optional[str] = None
    instance_id: Optional[str] = None
    instance_type: Optional[str] = None
    key_name: Optional[str] = None
    launch_time: Optional[str] = None
    monitoring: Optional[Monitoring] = None
    placement: Optional[Placement] = None
    private_dns_name: Optional[str] = None
    private_ip_address: Optional[str] = None
    product_codes: Optional[List[Any]] = None
    public_dns_name: Optional[str] = None
    public_ip_address: Optional[str] = None
    state: Optional[State] = None
    state_transition_reason: Optional[str] = None
    subnet_id: Optional[str] = None
    vpc_id: Optional[str] = None
    architecture: Optional[str] = None
    block_device_mappings: Optional[List[BlockDeviceMapping]] = None
    client_token: Optional[str] = None
    ebs_optimized: Optional[bool] = None
    ena_support: Optional[bool] = None
    hypervisor: Optional[str] = None
    network_interfaces: Optional[List[NetworkInterface]] = None
    root_device_name: Optional[str] = None
    root_device_type: Optional[str] = None
    security_groups: Optional[List[Group]] = None
    source_dest_check: Optional[bool] = None
    tags: Optional[List[Tag]] = None
    virtualization_type: Optional[str] = None
    cpu_options: Optional[CPUOptions] = None
    capacity_reservation_specification: Optional[CapacityReservationSpecification] = None
    hibernation_options: Optional[HibernationOptions] = None
    metadata_options: Optional[MetadataOptions] = None
    enclave_options: Optional[EnclaveOptions] = None
    platform_details: Optional[str] = None
    usage_operation: Optional[str] = None
    usage_operation_update_time: Optional[str] = None
