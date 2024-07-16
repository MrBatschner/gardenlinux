def test_nvme(client, with_nvme):
    """ Test for the root disk to be on an nvme device """
    (exit_code, output, error) = client.execute_command("findmnt -k -M / -J | jq -r '.filesystems[0].source'")
    assert exit_code == 0, f"no {error=} expected"
    assert "/dev/nvme" in output, f"root device is not /dev/nvme* but {output}"
