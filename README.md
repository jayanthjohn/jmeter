# Read container memory from cgroup
H2O_MEMORY_LIMIT_BYTES=$(cat /sys/fs/cgroup/memory/memory.limit_in_bytes)

# Subtract 700MB for RStudio
CALCULATED=$((H2O_MEMORY_LIMIT_BYTES - 1024*1024*700))

# Avoid negative heap size (set minimum 256m)
if [ $CALCULATED -lt $((256*1024*1024)) ]; then
  echo "WARNING: Container memory too low. Using minimum heap 256m."
  CALCULATED=$((256*1024*1024))
fi

# Convert bytes → MB for Java heap (Xmx)
H2O_MEMORY_LIMIT_MB=$((CALCULATED/1024/1024))

# Inject value into supervisord.conf
sudo sed -i "s/H2O_MEMORY_LIMIT/${H2O_MEMORY_LIMIT_MB}m/" /etc/supervisord.conf
