entity hello is
end entity hello;

architecture behavior of hello is
begin
    process
    begin
        report "Hello, GitHub!" severity note;
        wait;
    end process;
end architecture behavior;
